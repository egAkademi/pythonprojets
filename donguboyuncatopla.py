print("""""

1- çıkmak için q ye basın

""""")
toplam=0
while True:
     a = input("sayı: ")
     if (a=="q"):
         break
     a = int(a)
     toplam = toplam + a
print(toplam)


