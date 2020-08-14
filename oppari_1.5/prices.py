from binance.client import Client
from time import sleep
import keys

client = Client(keys.api_1, keys.api_2)

#Api symboli ( Kaupankäyntipari Binance coin (BNB) ja Tether (USDT) )
api_symbol = 'BNBUSDT'

def valuutan_tiedot():
    while True:
        #Valuuttaparin tiedot (1 minuutin "kynttilät" 200 minuutin ajalta )
        valuutta = client.get_historical_klines(api_symbol, Client.KLINE_INTERVAL_1MINUTE, "200 MIN ago UTC")

        #Varmistetaan datan olevan 200 minuutilta
        check = len(valuutta)
        if check == 200:

            #parsitaan saatuja tietoja ja siirretään tarvittavat tiedot uuteen taulukkoon
            i = -1
            lista = []
            #Lisätään taulukkoon ainoastaan sulkeutuneet hinnat ( closing prices )
            for x in valuutta:
                lista.append(valuutta[i][4])
                i -= 1
            #Muutetaan listan tiedot float-tyypeiksi    
            lista = [float(i) for i in lista]

            return lista
        
        print("Virhe datan saamisessa. Yritetään uudestaan------------------------------------------")
        sleep(2)



