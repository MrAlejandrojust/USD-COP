import yfinance as yf

import time

from os import system


def main():
    while True:
        # print('\nPrice is currently loading please wait...')
        usdcop = yf.download('USDCOP=X', period='1d')['Open']

        for k, v in usdcop.items():
            v = "{0:.2f}".format(v)
            print('\nCurrent Price:', v)

        time.sleep(10)
        system("cls")


if __name__ == "__main__":
    main()
