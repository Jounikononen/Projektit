#Osto- ja myyntifunctiot

def osta(client, quantity, api_symbol):
    print("ostetaan------------------------------------------")
    client.order_market_buy(symbol=api_symbol, quantity=quantity)
    balance = float(client.get_asset_balance(asset='BNB')['free'])
    print("Tilillä yhteensä: ", balance, " BNB")


def myy(client, api_symbol):
    balance = float(client.get_asset_balance(asset='BNB')['free'])
    balance = round(0.9*balance,1)    
    print("Myydään ",balance, " BNB------------------------------------------")
    client.order_market_sell(symbol=api_symbol, quantity=balance)
    print("Myyty! Odotetaan 60 sekuntia...")


