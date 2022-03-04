import yfinance as yf


from os import system


def main():
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
