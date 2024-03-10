import datetime as dt
now=dt.datetime.now()
hour= now.hour
minute=now.minute
if hour == '22':
    if minute=='00':
        pass
    #fiyatı kontrol et data da ki değerden farklı bir değerse 
    #yeni fiyatı 2. basamak olarak yaz ve farkını mail at fiyat her değiştiğinde 1. yi 2., 2.yi yeni fiyat değeri yap
