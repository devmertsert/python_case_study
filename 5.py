# Soru 5: Verilen listedeki None değerleri, kendinden önceki None olmayan değerle değiştirip yeni bir
# liste oluşturan fonksiyon yazınız. Ör: Input: [3, None, 2, None, None, 1, False, None, 10]
# Output: [3, 3, 2, 2, 2, 1 False, False, 10]. Listenin None ile başlamayacağını varsayabilirsiniz.

inputs = [3, None, 2, None, None, 1, False, None, 10]

def noneTemizle(liste):
    yeniliste = liste

    for i in range(0, len(liste)):
        if liste[i] == None:
            index = i - 1
            while liste[index] == None:
                index -= 1
            yeniliste[i] = liste[index]
    
    return yeniliste

print(noneTemizle(inputs))