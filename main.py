import yfinance as yf

import sched
import time
import threading

from os import system

# from interval import repeat_at_interval
# from interval import test


def main():
    # scheduler = sched.scheduler(time.time, time.sleep)
    # repeat_at_interval(scheduler, test, interval=60)
    # thread = threading.Thread(target=scheduler.run)
    # thread.start()
    try:
        while True:
            # print('\nPrice is currently loading please wait...')
            usdcop = yf.download('USDCOP=X', period='1d')['Open']

            for k, v in usdcop.items():
                v = "{0:.2f}".format(v)
                print('\nCurrent Price:', v)

            time.sleep(10)
            system("cls")
    except:
        print('\nSuccessfully stopped!')


if __name__ == "__main__":
    main()
