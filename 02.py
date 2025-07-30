import os
klasor_adi= input("Klasörün adini giriniz: ")

if not klasor_adi in os.listdir("."):

    print("Böyle bir klasör bulunmuyor. Ayni adla yeni klasör oluşturulsun mu? (e/h)")
    yeni_klasor= input().lower()

    if yeni_klasor == "e":
        
          os.mkdir(klasor_adi)
          print(f"{klasor_adi} klasörü oluşturuldu")