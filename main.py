import yfinance as yf

def main():
    print("Welcome to the Stock Info Interface, you will get the stock price history of whichever stock you enter!")
    stock: str = input("Stock: ")
    history: str = input("History (only '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', or 'max'): ")
    stock_price = getData(stock, history) 

    print(f"Price of {stock} {history} ago: ${stock_price.iloc[0]:.2f}")

def getData(stock, history):
    stock = yf.Ticker(stock)
    data = stock.history(period=(f"{history}"))
    
    return data['Close']
    
if __name__ == "__main__":
    main()
