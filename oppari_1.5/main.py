

import keys
import prices
import indicators
import action

from time import sleep

from binance.client import Client
from binance.websockets import BinanceSocketManager 

client = Client(api_key=keys.api_1, api_secret=keys.api_2)
bm = BinanceSocketManager(client)

#Pingaus
print(client.ping())

api_symbol = 'BNBUSDT' 
global balance
balance = float(client.get_asset_balance(asset='BNB')['free'])
balance2 = float(client.get_asset_balance(asset='USDT')['free'])
quantity = '0.6'

print("Tilillä yhteensä ", balance, " BNB")
print("Tilillä yhteensä ", balance2, " USDT")

#Haetaan historialliset tiedot viimeiseltä 200 minuutilta arrayhin
lista = prices.valuutan_tiedot()

kierros = 0

print("käynnistetään botti")
sleep(1)


def handle_message(msg):
    global kierros
    kierros += 1

    if msg['e'] == 'error':
        #Jos ilmenee ongelmia niin näytetään virheilmoitus ja jatketaan ohjelman ajoa mikäli mahdollista
        print(msg['m'])
        
    #Jos ei ole ongelmaa niin aletaan striimata tietoa reaaliajassa
    else:

        hinta = float(msg['k']['c'])
        lista[0] = hinta
        sma200, sma50 = indicators.sma(lista)

        if (kierros % 60 == 0):
            lista.pop()
            lista.insert(0, hinta)
            print("Lista päivitetty")

        print("----------------",kierros,"----------------")
        print("SMA50: ",sma50)
        print("SMA200: ",sma200)
        print("Hinta: ", hinta)


        balance = float(client.get_asset_balance(asset='BNB')['free'])

        #Jos tilillä alle 0.5BNB niin ostetaan
        if balance < 0.5:
            if sma50 < hinta:
                #Jos oston ehdot täyttyvät niin ajetaan osta-functio ( action.py - osta() )
                #Välitetään osta-functiolle client, quantity ja api-symbol
                action.osta(client,quantity,api_symbol)
                sleep(5)   
            else:
                print("Odotetaan ostoa")
        
        #Jos tilillä yli 0.5BNB niin myydään
        else:
            if sma50 > hinta:
                #Jos myynnin ehdot täyttyvät niin ajetaan myy-functio ( action.py - myy() )
                action.myy(client,api_symbol)
            else:
                print("Odotetaan myyntiä")

     
conn_key = bm.start_kline_socket('BNBUSDT', handle_message)
   
    
bm.start()

    
   
    

