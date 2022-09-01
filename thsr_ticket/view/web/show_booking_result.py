from typing import List

from thsr_ticket.view.web.abstract_show import AbstractShow
from thsr_ticket.view_model.booking_result import Ticket


class ShowBookingResult(AbstractShow):
    def show(self, tickets: List[Ticket], select: bool = False):
        ticket = tickets[0]
        print("\n\n----------- 訂位結果 -----------")
        print(f"訂位代號: {ticket.id}")
        print(f"繳費期限: {ticket.payment_deadline}")
        print(f"車次: {ticket.train_id}")
        print(f"出發時間: {ticket.depart_time}")
        print(f"座位: {ticket.seat_class}")
