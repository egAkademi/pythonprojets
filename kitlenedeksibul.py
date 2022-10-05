#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
denemesayisi = 3
while True:

    boy = float(input("Boyunuz: "))
    kilo = int(input("Kilonuz: "))

    kitlenendeksi= kilo/(boy*boy)
    print("Boyunuz: {}\nKilonuz: {}\nVücut Kitle Endeksi: {}\n".format(boy,kilo,kitlenendeksi))

    if kitlenendeksi<18.5 :
        print("18, 5 kg/m² ‘nin altındaki sonuçlar: İdeal kilonun altında")
        denemesayisi -= 1
    elif 18.5<kitlenendeksi<24.9 :
        print("18, 5 kg/m² ile 24, 9 kg/m² arasındaki sonuçlar: İdeal kiloda")
        denemesayisi -= 1
    elif 25<kitlenendeksi<29.9 :
        print("25 kg/m² ile 29, 9 kg/m² arasındaki sonuçlar: İdeal kilonun üstünde")
        denemesayisi -= 1
    elif 30<kitlenendeksi<39.9 :
        print("30 kg/m² ile 39, 9 kg/m² arasındaki sonuçlar: İdeal kilonun çok üstünde (obez)")
        denemesayisi -= 1
    elif kitlenendeksi>40 :
        print("İdeal kilonun çok üstünde (morbid obez)")
        denemesayisi -= 1
    if(denemesayisi==0) :
        print("deneme hakkınız bitti")
        break
