print(""""

******************
1-Dörtgen 
2-Üçgen
""""")

tip = input("Geometrik şekil tipi seçiniz: ")

if tip == "1" :
    a= float(input("birinci kenar: "))
    b = float(input("ikinci kenar: "))
    c = float(input("üçüncü kenar: "))
    d = float(input("dördüncü kenar: "))

    if a == b == c == d :
        print("Kare")
    elif a == b and c==d or a==c and b==d or a==d and b==c:
        print("Dikdörtgen")
    else:
        print("Dörtgen")

elif tip =="2":
    a= float(input("birinci kenar: "))
    b = float(input("ikinci kenar: "))
    c = float(input("üçüncü kenar: "))

    if a==b and a==c or b==a and b==c or c==a and c==b:
        print("İkizkenar")
    elif a==b==c:
        print("Eşkenar")
    elif a + b > c or a + c > b or b + c > a :
        print("Üçgen değil")
    else:
        print("Sıradan Üçgen")