# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 350,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("Enter stock symbols and quantities (type 'done' to finish):")

# Input stock symbols and quantities
while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in price list.")
        continue
    try:
        qty = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
print("\n=== Portfolio Summary ===")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Ask to save results
save_option = input("Do you want to save the result to a file? (yes/no): ").lower()

if save_option == 'yes':
    file_type = input("Choose file type (.txt or .csv): ").lower()
    filename = f"portfolio{file_type}"

    with open(filename, "w") as f:
        if file_type == '.csv':
            f.write("Stock,Quantity,Price,Value\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = price * qty
                f.write(f"{stock},{qty},{price},{value}\n")
            f.write(f",,,Total: ${total_investment}\n")
        else:
            f.write("=== Portfolio Summary ===\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = price * qty
                f.write(f"{stock}: {qty} shares x ${price} = ${value}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}\n")
    print(f"Portfolio saved to {filename}")
