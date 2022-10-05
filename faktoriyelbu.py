while True:
    a= int(input("sayı:"))

    faktoriyel=1
    for x in range(a,1,-1):
        faktoriyel = faktoriyel * x
    print(faktoriyel)
