import numpy as np
import pandas as pd
from numpy.random import randn

uretimTipleri = pd.DataFrame(data=randn(5,4) ,index = ["Makine Türü","Hazırlık Zamanları","Birim Üretim Zamanı","Süreçler","Parti Büyüklüğü"],columns=["Seri Üretim","Parti Tipi Üretim","Siparişe Göre Üretim","Proje Tipi Üretim"])
print(uretimTipleri)

uretimTipleri.loc["Makine Türü"]= ["Özel Amaçlı","Genel Amaçlı","Genel amaçlı","Genel Amaçlı"]
uretimTipleri.loc["Hazırlık Zamanları"]= ["Uzun","Değişken","Değişken","Değişken"]
uretimTipleri.loc["Birim Üretim Zamanı"]= ["Kısa","Değişken","Uzun","Uzun"]
uretimTipleri.loc["Süreçler"]= ["Ürün Bazlı","Değişken","Değişken","Proje Tipi"]
uretimTipleri.loc["Parti Büyüklüğü"]= ["Uygulanmaz","Var","Var","Uygulanmaz"]

print(uretimTipleri)

uretimTipleri["Özellikler"] = ["Makine Türü","Hazırlık Zamanları","Birim Üretim Zamanı","Süreçler","Parti Büyüklüğü"]
uretimTipleri.set_index("Özellikler",inplace=True)

print(uretimTipleri)
print(uretimTipleri.index.names)