import yfinance as yf


def main():
    while True:
        prices = yf.download('USDCOP=X', period='1d', )
        print(prices)

    # Enter TRM
    # TRM = "3,862.95"
    # diffence = TRM/prices
    # print(diffence)


if __name__ == '__main__':
    main()
