# Soru 4: Pozitif tam sayılar kümesinde kendisinden ve 1'den başka böleni olmayan sayılara
# asal sayılar denir. İlk on asal sayı 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 biçiminde sıralanır.
# 1. asal sayı 2, 10. asal sayı 29'dur. 10101. asal sayıyı bulan fonksiyonu yazınız.

def asalMi(sayi):
    if sayi < 2: return False
    if sayi == 2: return True
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True

def istenilenSiradakiAsaliBul(sira):
    sayac = 1
    sayi = 2
    while sayac <= sira:
        if asalMi(sayi):
            sayac += 1
        sayi += 1
    return sayi-1

print(istenilenSiradakiAsaliBul(10101))