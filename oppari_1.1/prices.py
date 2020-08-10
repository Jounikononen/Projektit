from binance.client import Client
from time import sleep
import keys

client = Client(keys.api_key, keys.api_secret)
#Api symbol
api_symbol = 'ETHUSDT'

def valuutan_tiedot():
    while True:
        #Ethereum valuutan tiedot (1minuutin kynttilät 15 minuutin ajalta)
        valuutta = client.get_historical_klines(api_symbol, Client.KLINE_INTERVAL_1MINUTE, "200 MIN ago UTC")
        check = len(valuutta)
        if check == 200:

            #Valuutan tiedot luettavampaan ja laskettavampaan muotoon
            i = -1
            lista = []
            for x in valuutta:
                lista.append(valuutta[i][4])
                i -= 1
            lista = [float(i) for i in lista]

            return lista
        
        print("Virhe datan saamisessa. Yritetään uudestaan------------------------------------------")
        sleep(2)


