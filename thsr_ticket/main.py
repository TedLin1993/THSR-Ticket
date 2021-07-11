from datetime import datetime ,date, timedelta
import time
import sys
sys.path.append("./")

from thsr_ticket.remote.endpoint_client import EndpointClient
from thsr_ticket.model.json.v1.train import Train
print("Loading model......")
from thsr_ticket.controller.booking_flow import BookingFlow


if __name__ == "__main__":
    #client = EndpointClient()
    #resp = client.get_trains_by_date("2020-01-25")
    #train = Train().from_json(resp[0])
    if len(sys.argv) == 3:
        flow = BookingFlow(sys.argv[1], sys.argv[2])
    elif len(sys.argv) >= 5:
        flow = BookingFlow(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        flow  = BookingFlow()
    
    # for time
    if len(sys.argv) == 6:
        book_date = datetime.strptime(sys.argv[5], "%Y-%m-%d").date()
        while (date.today()+timedelta(28)<book_date):
            print("Now is {}, waiting for {}...".format(datetime.now() ,book_date-timedelta(28)))
            time.sleep(1)
    result = flow.run()
