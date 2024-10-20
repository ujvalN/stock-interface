# Simple Stock Market Interface(SSMI)
## Video Demo: https://www.youtube.com/watch?v=Npy2_qlBSwU
## Description:
### Overview
This project is a Python-based tool designed to fetch, display, and analyze stock market data using the yfinance library. By providing stock symbols and a desired number of days for historical data, users can retrieve key financial metrics such as the stock's opening and closing prices, volume, market capitalization, P/E ratio, and dividend yield. Additionally, it allows users to review historical stock price data in an easy-to-read format.

### What I Did
The core functionality of the project centers around creating an interactive program that retrieves and displays stock market information from Yahoo Finance. The primary tasks I focused on include:

Data Retrieval: Using the yfinance library, the program fetches historical stock data based on user input. Users enter the stock ticker symbols (e.g., AAPL for Apple) and the number of days for which they want to see historical data.

Data Validation: The code checks whether the stock symbols are valid and whether the data can be retrieved. If invalid stock symbols are entered or no data is available, the program displays an error message.

Data Display: Once the stock data is retrieved, the program displays both the latest stock data (including opening price, closing price, high, low, and volume) and the company's additional financial details such as market capitalization, price-to-earnings (P/E) ratio, and dividend yield.

User Interaction: The program runs in a loop, allowing users to repeatedly fetch data for different stock symbols and time periods until they choose to exit. The stock symbols are entered in a comma-separated format, enabling users to check multiple stocks in one go.

Historical Data Output: The program provides a well-structured output of the historical stock prices for the specified number of days. This includes a table showing the stock's open, high, low, close, and volume values over the given period.

### What I Would Do to Improve
While the current implementation covers essential stock data retrieval and display, there were several features and improvements I initially wanted to implement but didn't due to complexity:

Graphical Visualization: I wanted to integrate a graphical representation of the stock data, such as line charts showing the stock's price trends over time. This could be done using libraries like matplotlib or plotly to visually display the stock's performance.

Real-Time Data Updates: Another feature I considered was incorporating real-time data updates. Instead of only fetching historical data, the program could have had a real-time ticker, updating the stock price every few seconds.

Enhanced Data Analysis: Beyond just retrieving and displaying stock data, I had ideas for integrating more advanced analytics. For example, calculating moving averages, identifying trends, or offering buy/sell recommendations based on the stock's historical performance.

User-Friendly Interface: Rather than a command-line interface, I thought of developing a GUI using frameworks like Tkinter or PyQt. This would make the program more accessible to users unfamiliar with the command line.

Error Handling and Testing: While basic error handling is included, I had plans to further refine it by ensuring that all edge cases were handled gracefully. For example, better handling for network issues, API rate limits, or more detailed feedback when invalid input is provided.

### What the Project Does
The project allows users to:

Fetch stock data for multiple stock symbols at once. Users can input a comma-separated list of stock symbols, and the program will retrieve and display the relevant data for each one.

View key stock details, including:

Opening price
Closing price
Highest and lowest prices for the day
Trading volume
Market capitalization
Forward P/E ratio
Dividend yield (if available)
Display historical stock data for a specified number of days. The data includes open, high, low, close, and volume for each trading day in the period.

Handle basic user errors. The program checks for invalid stock symbols and provides feedback when the symbol is incorrect or the data is unavailable.

How It Works
User Input: The user inputs a list of stock symbols (e.g., AAPL, TSLA) and specifies how many days of historical data they want to see.

Fetching Data: The yfinance library fetches the stock data from Yahoo Finance using the Ticker object. This retrieves historical data for the given period.

Displaying Data: The most recent stock data is displayed, followed by additional financial information and the full historical data for the specified period.

Error Handling: If the stock symbol is invalid or there is no data available for the given symbol, the program informs the user and prompts them to try again.

Looping: After the data is displayed, the program allows the user to enter more stock symbols or exit.

