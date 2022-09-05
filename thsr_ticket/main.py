from datetime import datetime ,date, timedelta
import time
from argparse import ArgumentParser
import sys
sys.path.append("./")

from thsr_ticket.controller.booking_flow import BookingFlow


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--id", help="身分證字號", type=str)
    parser.add_argument("--email", help="信箱", type=str)
    parser.add_argument("--phone", help="電話", type=str)
    parser.add_argument("--start_station", help="起始站 Ex. Taipei", type=str)
    parser.add_argument("--dest_station", help="終點站 Ex. Zuouing", type=str)
    parser.add_argument("--auto", help="是否自動完成所有流程 Ex. auto", type=str)
    parser.add_argument("--train_no", help="列車代號", type=str)
    parser.add_argument("--date", help="訂票日期 Ex. 2021/01/01", type=str)
    args = parser.parse_args()

    flow = BookingFlow(args)

    if args.date:
        book_date = datetime.strptime(args.date, "%Y/%m/%d").date()
        if book_date.weekday()<=4:
            # Monday to Friday
            while (date.today()+timedelta(28)<book_date):
                print("Now is {}, waiting for {}...".format(datetime.now() ,book_date-timedelta(28)))
                time.sleep(1)
        elif book_date.weekday()>=5:
            # Sunday
            while (date.today()+timedelta(24+book_date.weekday())<book_date):
                print("Now is {}, waiting for {}...".format(datetime.now() ,book_date-timedelta(24+book_date.weekday())))
                time.sleep(1)

    result = flow.run()
