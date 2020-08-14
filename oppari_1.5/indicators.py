#Indikaattorit (SMA)
#SMA50 ja SMA200 (Simple moving average)

def sma(lista):

    #SMA200 kaava
    sma200 = round(sum(lista) / len(lista),6)

    #Listan 50 tuoreinta arvoa (SMA50 varten))
    uusiLista = lista[0:-150]

    #SMA50 kaava
    sma50 = round(sum(uusiLista) / len(uusiLista),6)

    #Palautetaan pääohjelmalle SMA200 ja SMA50 arvot
    return sma200, sma50




    


    
