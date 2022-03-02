import yfinance as yf


def main():
    precios = yf.download('USDCOP=X', period='1d', )

    print(precios)


if __name__ == '__main__':
    main()
