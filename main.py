import yfinance as yf

def fetch_stock_data(symbol, days):
    stock = yf.Ticker(symbol)
    hist = stock.history(period=f'{days}d')  # Retrieve data for the specified number of days
    
    if hist.empty:
        print("Error: Invalid symbol or no data available.")
        return None

    return stock, hist

def display_stock_info(stock, hist, symbol):
    latest_data = hist.iloc[-1]
    print("\nStock Information:\n")
    print(f"Symbol: {symbol}")
    print(f"Open: {latest_data['Open']:.2f}")
    print(f"High: {latest_data['High']:.2f}")
    print(f"Low: {latest_data['Low']:.2f}")
    print(f"Close: {latest_data['Close']:.2f}")
    print(f"Volume: {latest_data['Volume']:,}")
    
    # Display additional information
    info = stock.info
    print(f"Market Cap: {info.get('marketCap', 'N/A')}")
    print(f"P/E Ratio: {info.get('forwardPE', 'N/A')}")
    print(f"Dividend Yield: {info.get('dividendYield', 'N/A'):.2%}")

    # Display historical data
    print("\nHistorical Data (Last {} Days):".format(len(hist)))
    print(hist[['Open', 'High', 'Low', 'Close', 'Volume']])

def main():
    while True:
        symbols = input("Enter stock symbols separated by commas (or 'exit' to quit): ").upper()
        if symbols == 'EXIT':
            break

        days = input("Enter number of days for historical data: ")
        
        try:
            days = int(days)
            if days <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number of days.")
            continue

        symbols = [s.strip() for s in symbols.split(',')]
        
        for symbol in symbols:
            stock_data = fetch_stock_data(symbol, days)
            if stock_data is not None:
                stock, hist = stock_data
                display_stock_info(stock, hist, symbol)
            print("\n" + "="*50 + "\n")

if __name__ == '__main__':
    main()

