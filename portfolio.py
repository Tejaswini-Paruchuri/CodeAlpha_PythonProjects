import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 330,
    "AMZN": 140
}

print("===================================")
print("     STOCK PORTFOLIO TRACKER")
print("===================================")

portfolio = []
total_investment = 0

n = int(input("Enter number of different stocks: "))

for i in range(n):

    stock = input("Enter Stock Symbol: ").upper()

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter Quantity: "))

    investment = stock_prices[stock] * quantity

    total_investment += investment

    portfolio.append([stock, quantity, investment])

print("\n------- Portfolio Summary -------")

for item in portfolio:
    print(f"{item[0]} : {item[1]} Shares -> ${item[2]}")

print("---------------------------------")
print("Total Investment = $", total_investment)

# Save TXT File
with open("portfolio.txt", "w") as file:

    file.write("Portfolio Summary\n\n")

    for item in portfolio:
        file.write(f"{item[0]} : {item[1]} Shares -> ${item[2]}\n")

    file.write(f"\nTotal Investment = ${total_investment}")

# Save CSV File
with open("portfolio.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Stock", "Quantity", "Investment"])

    for item in portfolio:
        writer.writerow(item)

    writer.writerow(["Total", "", total_investment])

print("\nPortfolio saved successfully!")