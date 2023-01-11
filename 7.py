# Soru 7: Adresteki (tiny.cc/isimListesi) türkçe isim listesini python ile download edip,
# alfabetik olarak sıralayınız. Sıralama işlemi için quicksort algoritmasını kullanınız.
# Tekrar eden isimleri siliniz. Her isim için, satır sırasını ve türkçe alfabedeki harf
# sırası toplamını çarpıp bir skor bulunuz. Bu işlemleri yapıp, toplam skoru dönen bir
# fonksiyon yazınız.
# Örnek input: ["ALİ", "ALİ", "AHMET"]
#       output: 113
# Çözüm: 1. sıradaki AHMET'in skoru 1 * (1+10+16+6+24) = 57, 2. sıradaki ALİ'nin
# skoru 2 * (1+15+12) = 56
# Skor toplamları 113

import requests
import locale

locale.setlocale(locale.LC_COLLATE, 'tr_TR.UTF-8')

uppercase = ["A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T", "U", "Ü", "V", "Y", "Z"]
lowercase = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]

def quickSort(liste):
    if len(liste) <= 1:
        return liste
    
    pivot = liste[len(liste) // 2]
    sol = [x for x in liste if locale.strcoll(x, pivot) < 0]
    orta = [x for x in liste if locale.strcoll(x, pivot) == 0]
    sag = [x for x in liste if locale.strcoll(x, pivot) > 0]
    return quickSort(sol) + orta + quickSort(sag)

def listeyiDuzenle(liste):
    liste = list(dict.fromkeys(liste))
    liste = quickSort(liste)
    return liste

def skorToplamı(liste):
    liste = listeyiDuzenle(liste)
    toplam = 0
    for i in range(0, len(liste)):
        araToplam = 0
        for j in liste[i]:
            if j in uppercase:
                araToplam += uppercase.index(j) + 1
            else:
                araToplam += lowercase.index(j) + 1
        toplam += (i + 1) * araToplam
    return toplam

x = requests.get('https://gist.githubusercontent.com/akarca/fd99fea898db82dc39c41d03d68c93b8/raw/db67136bf7431be047a2faaef95eff5bd5df2f03/isimler')
isimler = listeyiDuzenle(x.text.split())

print(skorToplamı(isimler))