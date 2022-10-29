import yfinance as yf

#Fetches the price of a stock
def pull_stock_price(company):
    try:
        ticker = yf.Ticker(company)
        price = ticker.history()['Close'].iloc[-1]
        return round(price, 2)
    except IndexError:
        return None

#Fetches either call or put option info for a company
def pull_option_info(company, opt_type):
    try:
        ticker = yf.Ticker(company)
        if opt_type == "call":
            recent = ticker.option_chain()[0].values[0]
            for o in ticker.option_chain()[0].values:
                if o[1] > recent[1]:
                    recent = o
            return (recent[2], recent[5])
        else:
            recent = ticker.option_chain()[1].values[0]
            for o in ticker.option_chain()[1].values:
                if o[1] > recent[1]:
                    recent = o
            return (recent[2], recent[5])
    except IndexError:
        return None

print(pull_stock_price(input("Company: ")))

