# Soru 6: Verilen cümledeki kelimelerin ortalama uzunluğunu bulan fonksiyon yazınız.
# ",.!?:;" gibi noktalama işaretlerini kelime uzunluğuna dahil etmeyiniz.
# ör: avg_len("Elma, portakal, armut") -> 5.66


def ortalama_kelime_uzunlugu(cumle):
    onemsizKarakterler = [",", ".", "!", "?", ":", ";"]

    cumle = cumle.strip()

    for i in onemsizKarakterler:
        cumle = cumle.replace(i, '')
    
    kelimeler = cumle.split()

    toplam = 0
    for i in kelimeler:
        toplam += len(i)
    
    return (toplam / (len(kelimeler)))


print(ortalama_kelime_uzunlugu("Elma, portakal, armut"))