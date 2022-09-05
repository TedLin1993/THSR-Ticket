from typing import Mapping, Any


BOOKING_PAGE: Mapping[str, Any] = {
    "security_code_img": {
        "id": "BookingS1Form_homeCaptcha_passCode"
    },
    "seat_prefer_radio": {
        "id": "seatRadio0"
    }
}

ERROR_FEEDBACK: Mapping[str, Any] = {
    "error_content": {
        "name": "div",
        "attrs": {
            "class": "error-content"
        }
    },
    "feedbackPanelERROR": {
        "name": "span",
        "attrs": {
            "class": "feedbackPanelERROR"
        }
    }
}

TICKET_CONFIRMATION: Mapping[str, Any] = {
    "id_input_radio": {
        "id": "idInputRadio1"
    },
    "mobile_input_radio": {
        "id": "mobileInputRadio"
    }
}

BOOKING_RESULT: Mapping[str, Any] = {
    "ticket_id": {
        "name": "p",
        "attrs": {
            "class": "pnr-code"
        }
    },
    "payment_deadline": {
        "text": "（付款期限："
    },
    "seat_class": {
        "name": "div",
        "attrs": {
            "class": "seat-label"
        }
    },
    "train_id": {
        "name": "span",
        "attrs": {
            "id": "setTrainCode0"
        }
    },
    "depart_time": {
        "name": "span",
        "attrs": {
            "id": "setTrainDeparture0"
        }
    },
}
