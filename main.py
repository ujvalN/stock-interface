
import yfinance as yf

def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period='5d')  # Retrieve last 5 days of data
    
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

    # Display historical data for the last 5 days
    print("\nHistorical Data (Last 5 Days):")
    print(hist[['Open', 'High', 'Low', 'Close', 'Volume']])

def main():
    while True:
        symbols = input("Enter stock symbols separated by commas (or 'exit' to quit): ").upper()
        if symbols == 'EXIT':
            break
        
        symbols = [s.strip() for s in symbols.split(',')]
        
        for symbol in symbols:
            stock_data = fetch_stock_data(symbol)
            if stock_data is not None:
                stock, hist = stock_data
                display_stock_info(stock, hist, symbol)
            print("\n" + "="*50 + "\n")

if __name__ == '__main__':
    main()

