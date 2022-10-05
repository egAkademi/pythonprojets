def tam_sayibolenleribul(sayi):
    tam_bolenler = []

    for i in range(2,sayi):
        if(sayi%i==0):
            tam_bolenler.append(i)
    return tam_bolenler

while True:
    sayı = input("Sayı: ")

    if(sayı=="q"):
        print("çıktınız")
        break
    else:
        sayı=int(sayı)
        print("Tam bölen sayılar:", tam_sayibolenleribul(sayı))