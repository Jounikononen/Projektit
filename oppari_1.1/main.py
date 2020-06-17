from binance.client import Client
from time import sleep
import keys
import prices
import indicators

#Yhdistä Binanceen
client = Client(keys.api_key, keys.api_secret)

#Ping
print(client.ping())



api_symbol = 'ETHUSDT' 
balance = client.get_asset_balance(asset='ETH')['free']
balance2 = client.get_asset_balance(asset='USDT')['free']
quantity = '0.1'

print("Tilillä yhteensä ", balance, " ETH")
print("Tilillä yhteensä ", balance2, " USDT")

osto_lkm = 0
myynti_lkm = 0

#Osto
osto = True
while osto == True:

    #Valuutan arvot viimeiseltä 200 minuutilta (1 minuutin kynttilät)
    valuutan_tiedot = prices.valuutan_tiedot()
    #Hinta nyt
    price = valuutan_tiedot[0]
    #Simple moving averages (200 ja 50)
    sma200, sma50 = indicators.sma(valuutan_tiedot)
    print("Hinta nyt: ", price)
    balance = client.get_asset_balance(asset='ETH')['free']
    #Osto
    if float(balance) == 0:
        print("Kierros: ",osto_lkm) 
        if (sma50 > sma200 and sma50 < price):
            print("ostetaan------------------------------------------")
            client.order_market_buy(symbol=api_symbol, quantity=quantity)
            balance = client.get_asset_balance(asset='ETH')['free']
            print("Tilillä yhteensä ", balance, " ETH")
            osto_lkm = 0
            sleep(5)
  
        else:
            print("Odotetaan ostoa...")
            print("-------------------")
            osto_lkm += 1
            sleep(3)
            

    #Myynti
    else:
        print("Kierros: ",myynti_lkm)
        if myynti_lkm == 0:
            #Tallennetaan oston hinta 
            print("Eka kierros myyntiä!")
            osto_historia = client.get_my_trades(symbol=api_symbol)
            oston_hinta = indicators.stop_loss(osto_historia)
            print("Valuuttaa ostettu hintaan: ",oston_hinta)
            print("-------------------")
            sleep(3)

        else:
            erotus = float(oston_hinta) - price
            print('oston ja nykyisen hinnan erotus on: ', erotus)
        
            if (sma50 >= price or erotus >= 0.10):
                print("myydään------------------------------------------")
                balance = client.get_asset_balance(asset='ETH')['free']
                client.order_market_sell(symbol=api_symbol, quantity=balance)
                myynti_lkm = 0

            else:
                print("Odotetaan myyntiä...")
                print("-------------------")
                
                sleep(3)
    myynti_lkm += 1
