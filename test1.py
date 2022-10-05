print ("""""

*******
 liste
""""")

list = ["Gökhan Şit","Esra Şit"]

while True:

    yenikisi = input("Ad soyad giriniz")

    list.append(yenikisi)

    print(list)
    print(" 1.kişi {}\n 2.kişi {}\n 3.kişi {}\n".format(list[0],list[1],list[2]))