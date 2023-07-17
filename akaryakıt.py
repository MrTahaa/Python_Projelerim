#Kullanıcıdan aldığı şehir bilgisi ve görmek istediği  benzin,lpg ve dizel bilgisini alan
#buna bağlı olarak internetten çektiği bilgileri gösteren bir program yazınız
import http.client
import json
liste_benzin = []
liste_lpg = []
liste_dizel = []
def Benzin(city):
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 0MeJYeRX9OBEjk71cQDHk7:52DK1wAOBdV00slYB3Ko76"
        }

    conn.request("GET", "/gasPrice/turkeyGasoline?district=kadikoy&city="+city, headers=headers)

    res = conn.getresponse()
    data = res.read()
    veri1 = json.loads(data)
    for i in veri1["result"]:
        liste_benzin.append(i)
    

def lpg(city):
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 0MeJYeRX9OBEjk71cQDHk7:52DK1wAOBdV00slYB3Ko76"
        }

    conn.request("GET", "/gasPrice/turkeyLpg?city="+city, headers=headers)

    res = conn.getresponse()
    data = res.read()
    veri2 = json.loads(data)
    for i in veri2["result"]:
        liste_lpg.append(i)

def dizel(city):
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 0MeJYeRX9OBEjk71cQDHk7:52DK1wAOBdV00slYB3Ko76"
        }

    conn.request("GET", "/gasPrice/turkeyDiesel?district=kadikoy&city="+city, headers=headers)

    res = conn.getresponse()
    data = res.read()
    veri3 = json.loads(data)
    for i in veri3["result"]:
        liste_dizel.append(i)

bcity = input("Hangi şehrin akaryakıt fiyatlarını görmek istiyorsunuz:")
city = bcity.lower()
akaryakıt = int(input("Hangi akaryakıtın fiyatını görmek istersiniz\n1)Benzin\n2)LPG\n3)Dizel\n"))
if akaryakıt == 1:
    Benzin(city)
    for i in range(0,len(liste_benzin)):
        print(liste_benzin[i]["marka"],liste_benzin[i]["benzin"])
elif akaryakıt == 2:
    lpg(city)
    for i in range(0,len(liste_benzin)):
        print(liste_lpg[i]["marka"],liste_lpg[i]["lpg"])
elif akaryakıt == 3:
    dizel(city)
    for i in range(0,len(liste_benzin)):
        print(liste_dizel[i]["marka"],liste_dizel[i]["dizel"])










    
