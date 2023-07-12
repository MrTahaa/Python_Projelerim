#Mutlu bir sayı, aş̧ağıdaki süreç tarafından tanımlanan bir sayıdır:
#1. Herhangi bir pozitif tamsayıyı basamaklarının karelerinin toplamını bulun.
#2. Bulunan bu sayıya tekrar 1. Adımı sonunda 1 olmayacak şekilde tekrarlayın
#3. Bu iş̧lemin (1) de bittiği sayılar mutlu sayılardır.
#Örnek sayı : n = 19
#1**2 + 9**2 =82
#8**2 + 2**2 =68
#6**2 + 8**2 =100
#1**2 + 0**2 + 0**2 =1
liste= []
def Mutlu_Sayi(sayi):
    toplam = 0
    for i in sayi:
        toplam += int(i)**2
    if str(toplam) == 1:
        print("Kontrol edilen sayı mutlu sayıdır")
    else:
        if liste.count(str(toplam)) == 1:
            print("Kontrol edilen sayı mutlu sayı değildir")
        else:
            toplam = str(toplam)
            liste.append(toplam)
            return Mutlu_Sayi(toplam)
          
sayi = input("Mutlu sayı olup olmadığı kontrol edilecek sayıyı giriniz ")
liste.append(sayi)
Mutlu_Sayi(sayi)
