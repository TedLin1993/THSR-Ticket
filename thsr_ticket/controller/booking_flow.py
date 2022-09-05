import io
from PIL import Image
from requests.models import Response
import ddddocr
import time

from thsr_ticket.remote.http_request import HTTPRequest
from thsr_ticket.model.web.booking_form.booking_form import BookingForm
from thsr_ticket.model.web.booking_form.ticket_num import AdultTicket
from thsr_ticket.model.web.confirm_train import ConfirmTrain
from thsr_ticket.model.web.confirm_ticket import ConfirmTicket
from thsr_ticket.view_model.avail_trains import AvailTrains
from thsr_ticket.view_model.error_feedback import ErrorFeedback
from thsr_ticket.view_model.booking_result import BookingResult
from thsr_ticket.view.web.booking_form_info import BookingFormInfo
from thsr_ticket.view.web.show_avail_trains import ShowAvailTrains
from thsr_ticket.view.web.show_error_msg import ShowErrorMsg
from thsr_ticket.view.web.confirm_ticket_info import ConfirmTicketInfo
from thsr_ticket.view.web.show_booking_result import ShowBookingResult
from thsr_ticket.view.common import history_info
from thsr_ticket.model.db import ParamDB, Record


class BookingFlow:
    def __init__(self, args) -> None:
        self.start_station = args.start_station
        self.dest_station = args.dest_station
        self.train_no = args.train_no
        self.outBoundDate = args.date
        self.inBoundDate = args.date
        self.outBoundTime = args.time

        self.id = args.id
        self.phone = args.phone

        self.client = HTTPRequest()

        self.book_form = BookingForm()
        self.book_info = BookingFormInfo()

        self.confirm_train = ConfirmTrain()
        self.show_avail_trains = ShowAvailTrains()

        self.confirm_ticket = ConfirmTicket()
        self.confirm_ticket_info = ConfirmTicketInfo()

        self.error_feedback = ErrorFeedback()
        self.show_error_msg = ShowErrorMsg()

        self.db = ParamDB()
        self.record = Record()

        self.ocr = ddddocr.DdddOcr()

    def run(self) -> Response:
        self.set_start_station()
        self.set_dest_station()
        self.book_form.outbound_date = self.outBoundDate
        self.book_form.inbound_date = self.inBoundDate
        self.set_prefer_window_seat(False)
        self.set_booking_method(self.train_no is not None)
        self.set_search_by()
        self.set_outbound_time()
        self.set_adult_ticket_num()
        
        while True:
            while True:
                # First page. Booking options
                self.book_form.security_code = self.input_security_code()
                form_params = self.book_form.get_params()
                result = self.client.submit_booking_form(form_params)
                if not self.show_error(result.content):
                    break
                self.client = HTTPRequest()
            if self.train_no is not None:
                break

            # Second page. Train confirmation
            # This page is only required for selecting by time
            self.confirm_train.selection = "radio18" # Select first train
            confirm_params = self.confirm_train.get_params()
            result = self.client.submit_train(confirm_params).content
            if not self.show_error(result):
                break
            self.client = HTTPRequest()
            time.sleep(1)

        # Third page. Ticket confirmation
        self.set_personal_id()
        self.set_phone()
        self.set_passenger_num()
        ticket_params = self.confirm_ticket.get_params()
        result = self.client.submit_ticket(ticket_params, (self.train_no is not None))
        if self.show_error(result.content):
            return result

        result_model = BookingResult().parse(result.content)
        book = ShowBookingResult()
        book.show(result_model)

        print("\n請使用官方提供的管道完成後續付款以及取票!!")

        self.db.save(self.book_form, self.confirm_ticket)
        return result

    def show_history(self) -> None:
        hist = self.db.get_history()
        h_idx = history_info(hist)
        if h_idx is not None:
            self.record = hist[h_idx]

    def set_start_station(self) -> None:
        if self.record.start_station is not None:
            self.book_form.start_station = self.record.start_station
        else:
            self.book_form.start_station = self.book_info.station_info("啟程", self.start_station)

    def set_dest_station(self) -> None:
        if self.record.dest_station is not None:
            self.book_form.dest_station = self.record.dest_station
        else:
            self.book_form.dest_station = self.book_form.dest_station = self.book_info.station_info("到達", self.dest_station)

    def set_outbound_time(self) -> None:
        if self.record.outbound_time is not None:
            self.book_form.outbound_time = self.record.outbound_time
        elif self.outBoundTime is not None:
            self.book_form.outbound_time = self.outBoundTime
        else:
            self.book_form.outbound_time = self.book_info.time_table_info()

    def set_prefer_window_seat(self, by_window=False) -> None:
        if by_window:
            self.book_form.seat_prefer = "radio19"

    def set_booking_method(self, by_trainId=False) -> None:
        if by_trainId:
            self.book_form.booking_method = "radio29"

    def set_search_by(self) -> None:
        if self.train_no is not None:
            self.book_form.search_by = 1
            self.book_form.train_no = self.train_no

    def set_adult_ticket_num(self) -> None:
        if self.record.adult_num is not None:
            self.book_form.adult_ticket_num = self.record.adult_num
        else:
            # Only select one ticket
            self.sel = self.book_info.ticket_num_info("大人", default_value=1, select=False)
            self.book_form.adult_ticket_num = AdultTicket().get_code(self.sel)

    def set_personal_id(self) -> None:
        if self.record.personal_id is not None:
            self.confirm_ticket.personal_id = self.record.personal_id
        else:
            self.confirm_ticket.personal_id = self.confirm_ticket_info.personal_id_info(self.id, False)

    def set_phone(self) -> None:
        if self.record.phone is not None:
            self.confirm_ticket.phone = self.record.phone
        else:
            self.confirm_ticket.phone = self.confirm_ticket_info.phone_info(self.phone, False)

    def set_passenger_num(self) -> None:
        self.confirm_ticket.passenger_count = self.sel

    def input_security_code(self) -> str:
        book_page = self.client.request_booking_page()
        img_resp = self.client.request_security_code_img(book_page.content)
        if img_resp:
            code = self.ocr.classification(img_resp.content)
        else:
            code = ''
        print("輸入驗證碼: {}".format(code))
        return code

    def show_error(self, html: bytes) -> bool:
        errors = self.error_feedback.parse(html)
        if len(errors) == 0:
            return False

        self.show_error_msg.show(errors)
        self.error_feedback = ErrorFeedback()
        return True
