import yfinance as yf

from bs4 import BeautifulSoup
import requests

import time

from os import system


def main():
    # Today TRM
    URL = 'https://www.trmhoy.co/en/'
    req = requests.get(URL)

    status_code = req.status_code

    if status_code == 200:
        html = BeautifulSoup(req.text, "html.parser")
        trm_class = html.find('div', {'class': 'col-4 col-12-medium'})
        trm_today = trm_class.find('h2').getText()

    # Real Time TRM
    while True:
        usdcop = yf.download('USDCOP=X', period='1d')['Open']

        for k, v in usdcop.items():
            v = "{0:.2f}".format(v)
            print('\nRT Price: $' + v)

        print('TRM Today:', trm_today)

        try:
            time.sleep(10)
            system("cls")
        except:
            system("cls")


if __name__ == "__main__":
    main()
