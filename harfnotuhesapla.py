# Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
#
#     Vize1 toplam notun %30'una etki edecek.
#
#     Vize2 toplam notun %30'una etki edecek.
#
#     Final toplam notun %40'ına etki edecek.

vize1 = float(input("Vize 1 :"))
vize2 = float(input("Vize 2 :"))
final = float(input("Final :"))

toplamnot = vize1 * 0.3 + vize2 * 0.3 + final * 0.4

if toplamnot >= 90:
    print("AA")
elif toplamnot >=85:
    print("BA")
elif toplamnot >=80:
    print("BB")
elif toplamnot >=75:
    print("CB")
elif toplamnot >= 70:
    print("CC")
elif toplamnot >= 65:
    print("DC")
elif toplamnot >= 60:
    print("DD")
elif toplamnot >= 55:
    print("FD")
elif toplamnot < 55:
    print("FF")
else:
    print("Geçersiz")