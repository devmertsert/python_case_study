# Soru 2: 5 milyondan küçük 3'e bölünebilen Fibonacci sayılarının toplamını bulan fonksiyon yazınız


# Fibonacci formülü:
# F(n) = F(n-1) + F(n-2)
# Örnek:
# F(2) = F(1) + F(0)
# F(3) = F(2) + F(1)
# F(4) = F(3) + F(2)
# 1 1 2 3 5 8 13 21 34 55 ...


def uce_bolunen_fibonacciler_toplami(maksimum):
    sayi1 = 0
    sayi2 = 1
    toplam = 0

    while sayi2 < maksimum:
        if sayi2 % 3 == 0:
            toplam += sayi2
        gecici = sayi1
        sayi1 = sayi2
        sayi2 += gecici
    
    return toplam

print(uce_bolunen_fibonacciler_toplami(5000000))