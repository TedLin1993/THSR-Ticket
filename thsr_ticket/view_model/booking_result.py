from typing import List, Mapping, Any
from collections import namedtuple

from bs4 import BeautifulSoup

from thsr_ticket.view_model.abstract_view_model import AbstractViewModel
from thsr_ticket.configs.web.parse_html_element import BOOKING_RESULT

Ticket = namedtuple("Ticket", [
        "id", "seat_class", "payment_deadline", "train_id", "depart_time"
])


class BookingResult(AbstractViewModel):
    def __init__(self) -> None:
        super(BookingResult, self).__init__()
        self.ticket: Ticket = None

    def parse(self, html: bytes) -> List[Ticket]:
        page = self._parser(html)
        ticket_id = page.find(**BOOKING_RESULT["ticket_id"]).find("span").contents[0]
        deadline = page.find(**BOOKING_RESULT["payment_deadline"]).find_next().text
        seat_class = page.find(**BOOKING_RESULT["seat_class"]).find("span").contents[0]
        train_id = page.find(**BOOKING_RESULT["train_id"]).contents[0]
        depart_time = page.find(**BOOKING_RESULT["depart_time"]).contents[0]
        self.ticket = Ticket(
            id=ticket_id,
            payment_deadline=deadline,
            seat_class=seat_class,
            train_id=train_id,
            depart_time=depart_time
        )
        return [self.ticket]