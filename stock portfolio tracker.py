#STOCK PORTFOLIO TRACKER

#HARCODED STOCK PRICE

stock_prices={
    "AAPL":180,
    "TSLA":250,
    "GOOGL":140,
    "MSFT":420,
    "AMZN":190
}
total_investment = 0
portfolio = {}

#NUMBER OF STOCKS USER WANTS TO ENTER 

n = int(input("How many different stocks do you own?: "))
for i in range(n):
    stock = input("\n Enter stock symbol (AAPL, TSLA, GOOGL , MSFT , AMZN):").upper()
    quantity = int(input("Enter Quantity:"))

if stock in stock_prices:
    value = stock_prices[stock]*quantity
    portfolio[stock] = quantity
    total_investment += value
else:
    print("Stock not found!")

#DISPLAY PORTFOLIO

print("\n -----Portfolio Summary------")  
for stock,quantity in portfolio.items():
    print(f"{stock}:{quantity} shares * ${stock_prices[stock]} = ${quantity * stock_prices[stock]}")

print(f"\n Total Investment Value:${total_investment}")

#SAVE RESULT TO A TEXT FILE

with open ("portfolio.txt","w") as file:
    file.write("Portfolio Summary\n")
    file.write("--------------\n")

for stock , quantity in portfolio.items():
    file.write(f"{stock}:{quantity} shares = ${quantity*stock_prices[stock]}\n")
    file.write(f"\nTotal Investment Value:${total_investment}")

    print("\nPortfolio saved to portfolio.txt")
