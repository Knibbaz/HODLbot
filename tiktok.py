import os
from dotenv import load_dotenv, find_dotenv
import bitvavo

EXCHANGE = os.environ.get('EXCHANGE')
if EXCHANGE == "Bitvavo": exchange = bitvavo

# Only allow numbers
verschillendePercentages = int(input("Hoeveel verschillende percentages wil je instellen? "))
counter = 0
coins = []

balance = exchange.getBalance()

for coin in balance:
    if float(coin["available"]) > 0:
        koopPrijs = float(
            input("Wat was de koopprijs van " + coin["symbol"] + "? "))
        if koopPrijs > 0:
            coins.append({"symbool": coin["symbol"], "prijs": koopPrijs, "muntjes": float(coin["available"])})

while counter < verschillendePercentages:
    stijging = float(input("Na hoeveel procent stijging wil je muntjes verkopen? "))
    percentageVerkopen = float(input("Hoeveel procent van je muntjes wil je dan verkopen? "))

    for coin in coins:
        targetPrice = int(round(coin['prijs'] / 100 * (100 + stijging), 0))
        amount = float(round(coin['muntjes'] / 100 * percentageVerkopen, 3))
        
        coin['muntjes'] = coin['muntjes'] - amount
        
        print(exchange.placeLimitOrder("ETH", "sell", amount, targetPrice))

    counter += 1