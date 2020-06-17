#Indikaattorit (RSI, SMA, stop_loss)

#SMA50 ja SMA200 (Simple moving average)
def sma(lista):

    #SMA200 kaava
    sma200 = round(sum(lista) / len(lista),6)
    print("SMA200: ", sma200)
    #Listan 50 tuoreinta arvoa
    uusiLista = lista[0:-150]

    #SMA50 kaava
    sma50 = round(sum(uusiLista) / len(uusiLista),6)
    print("SMA50: ", sma50)

    #Palautetaan SMA200 ja SMA50 arvot
    return sma200, sma50


#Viimeisin toteutunut osto ja sen hinta
def stop_loss(historia):
    i = -1
    loop = True
    while loop == True:
        osto = historia[i]
        tieto = osto['isBuyer']
        if tieto == True:
            #Palautetaan viimeisimmän oston hinta
            return osto['price']
        else:
            i -= 1
   



    


    
