# tracker.py

# Hardcoded dictionary with stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2900,
    "AMZN": 135,
    "MSFT": 310
}

portfolio = {}
total_investment = 0

# Input loop
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
print("\n----- Investment Summary -----")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    print(f"{stock}: {qty} shares × ₹{price} = ₹{investment}")
    total_investment += investment

print(f"\nTotal Investment: ₹{total_investment}")

# Optional: Save to a text file
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("investment_summary.txt", "w") as f:
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            f.write(f"{stock}: {qty} shares × ₹{price} = ₹{investment}\n")
        f.write(f"\nTotal Investment: ₹{total_investment}")
    print("Summary saved to investment_summary.txt")
