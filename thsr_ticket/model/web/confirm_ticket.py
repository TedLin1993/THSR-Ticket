from typing import Mapping, Any
from jsonschema import validate

from thsr_ticket.model.web.abstract_params import AbstractParams
from thsr_ticket.configs.web.param_schema import CONFIRM_TICKET_SHEMA


class ConfirmTicket(AbstractParams):
    def __init__(self) -> None:
        self._personal_id: str = None
        self._phone: str = ""
        self._passenger_count: int = 1

    def get_params(self, val: bool = True) -> Mapping[str, Any]:
        params = {
            "BookingS3FormSP:hf:0": "",
            "diffOver": 1,
            "isSPromotion": 1,
            "passengerCount": self._passenger_count,
            "isGoBackM": "",
            "backHome": "",
            "TgoError": "1",
            "idInputRadio": 0,
            "dummyId": self._personal_id,
            "dummyPhone": self._phone,
            "email": "",
            "TicketMemberSystemInputPanel:TakerMemberSystemDataView:memberSystemRadioGroup": "radio40",
            "agree": "on"
        }

        if val:
            validate(params, schema=CONFIRM_TICKET_SHEMA)
        return params

    @property
    def personal_id(self) -> str:
        return self._personal_id

    @personal_id.setter
    def personal_id(self, value: str) -> None:
        if len(value) != 10:
            raise ValueError("Wrong length of R.O.C. ID. Should be 10, received {}".format(len(value)))
        self._personal_id = value

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        if len(value) != 0 and len(value) != 10:
            raise ValueError("Wrong length of phone number. Should be 10, received {}".format(len(value)))
        if len(value) != 0 and not value.startswith("09"):
            raise ValueError("Wrong prefix with the phone number: {}".format(value))
        self._phone = value

    @property
    def passenger_count(self) -> int:
        return self._passenger_count

    @passenger_count.setter
    def passenger_count(self, value: int) -> None:
        self._passenger_count = value