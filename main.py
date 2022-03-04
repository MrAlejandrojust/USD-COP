import yfinance as yf

import sched
import time
import threading

from interval import repeat_at_interval
from interval import test


def main():
    # scheduler = sched.scheduler(time.time, time.sleep)
    # repeat_at_interval(scheduler, test, interval=60)
    # thread = threading.Thread(target=scheduler.run)
    # thread.start()
    try:
        while True:
            time.sleep(10)
            usdcop = yf.download('USDCOP=X', period='1d')['Open']
            print(usdcop)
    except:
        print('\nSuccessfully stopped!')


if __name__ == "__main__":
    main()
