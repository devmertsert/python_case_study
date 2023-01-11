# Soru 3: Baştan ve sondan yazıldığında değişmeyen sayılara palindrom sayılar denir
# Ör: 1001, 23432. 2 haneli sayıların çarpımından elde edilen en büyük palindrom
# sayısı 91 * 99 = 9009'dur. 3 haneli sayıların çarpımından elde edilen en büyük
# palindrom sayısını bulan fonksiyonu yazınız

def enBuyukPalindromBul(haneSayisi):
    if haneSayisi < 1:
        print(False)
        return
    enKucukSayi = 0
    if haneSayisi > 1:
        enKucukSayi = int('1' + ('0' * (haneSayisi - 1)))
    enBuyukSayi = int('9' * haneSayisi)

    enBuyuk = [0, 0, 0]
    for i in range(enBuyukSayi, enKucukSayi - 1, -1):
        for j in range(i, enKucukSayi - 1, -1):
            sayi = i * j
            if str(sayi) == str(sayi)[::-1]:
                if sayi > enBuyuk[2]:
                    enBuyuk = [i, j, sayi]
    
    print(enBuyuk[0], "*", enBuyuk[1], "*", enBuyuk[2])

enBuyukPalindromBul(3)