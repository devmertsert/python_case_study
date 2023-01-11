# Python Case Study

## Sorular
- Soru 1: Asal çarpanları sadece 2, 3 ya da 5'ten oluşan 1milyon'dan küçük doğal sayıların toplamını bulan fonksiyon yazınız. Asal çarpanı 2, 3 ya da 5 olan sayilar: 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20 ...
- Soru 2: 5 milyondan küçük 3'e bölünebilen Fibonacci sayılarının toplamını bulan fonksiyon yazınız
- Soru 3: Baştan ve sondan yazıldığında değişmeyen sayılara palindrom sayılar denir Ör: 1001, 23432. 2 haneli sayıların çarpımından elde edilen en büyük palindrom sayısı 91 * 99 = 9009'dur. 3 haneli sayıların çarpımından elde edilen en büyük palindrom sayısını bulan fonksiyonu yazınız
- Soru 4: Pozitif tam sayılar kümesinde kendisinden ve 1'den başka böleni olmayan sayılara asal sayılar denir. İlk on asal sayı 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 biçiminde sıralanır. 1. asal sayı 2, 10. asal sayı 29'dur. 10101. asal sayıyı bulan fonksiyonu yazınız.
- Soru 5: Verilen listedeki None değerleri, kendinden önceki None olmayan değerle değiştirip yeni bir liste oluşturan fonksiyon yazınız. Ör: Input: [3, None, 2, None, None, 1, False, None, 10] Output: [3, 3, 2, 2, 2, 1 False, False, 10]. Listenin None ile başlamayacağını varsayabilirsiniz.
- Soru 6: Verilen cümledeki kelimelerin ortalama uzunluğunu bulan fonksiyon yazınız. ",.!?:;" gibi noktalama işaretlerini kelime uzunluğuna dahil etmeyiniz. ör: avg_len("Elma, portakal, armut") -> 5.66
- Soru 7: Adresteki (tiny.cc/isimListesi) türkçe isim listesini python ile download edip, alfabetik olarak sıralayınız. Sıralama işlemi için quicksort algoritmasını kullanınız. Tekrar eden isimleri siliniz. Her isim için, satır sırasını ve türkçe alfabedeki harf sırası toplamını çarpıp bir skor bulunuz. Bu işlemleri yapıp, toplam skoru dönen bir fonksiyon yazınız. Örnek input: ["ALİ", "ALİ", "AHMET"]
output: 113
Çözüm: 1. sıradaki AHMET'in skoru 1 * (1+10+16+6+24) = 57, 2. sıradaki ALİ'nin skoru 2 * (1+15+12) = 56 Skor toplamları 113

## Kurulum
Projeyi çalıştırabilmek için aşağıdaki adımları uygulayınız.

```sh
git clone https://github.com/devmertsert/python_case_study.git
```
```sh
cd python_case_study
```
```sh
pip install -r requirements.txt
```

Ardından çalıştırmak istediğiniz sorunun bulunduğu python dosyasını aşağıdaki komutla çalıştırınız (Örnek 1. soru için)

```sh
python 1.py
```