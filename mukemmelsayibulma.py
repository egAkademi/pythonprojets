while True:
    a= int(input("sayı:"))
    toplam = 0
    x=1
    for x in range(a-1, 0, -1):
        if(a % x == 0):
            print(x)
            toplam += x
    if(toplam==a):
        print("mükemmel")
    else:
        print("değil")
        break
