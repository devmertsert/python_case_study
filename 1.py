# Soru 1: Asal çarpanları sadece 2, 3 ya da 5'ten oluşan 1milyon'dan küçük doğal
# sayıların toplamını bulan fonksiyon yazınız. Asal çarpanı 2, 3 ya da 5 olan
# sayilar: 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20 ...



# asal çarpanlara bölme işlemi:
# sayi 2 den başlayarak sırasıyla gelen asal sayılara bölünerek bulunur
# örnek olarak sayı 2 ye bölünemeyene kadar 2 ye bölünür ardından aynı
# için uygulanır ve sonuç olarak 1 e ulaşıldığında tüm bölmüş olduğumuz
# sayıları bize bölünebilen asal sayıları verir

def bol(bolunen, bolen):
    while bolunen % bolen == 0:
        bolunen /= bolen
    return bolunen

def toplamlariBul(sayi):
    asalBolenler = [2, 3, 5]
    toplam = 0

    for i in range(2, sayi + 1):
        kontrolSayi = i

        for asalSayi in asalBolenler:
            kontrolSayi = bol(kontrolSayi, asalSayi)

        if kontrolSayi == 1:
            toplam += i
    
    return toplam

print(toplamlariBul(1000000))