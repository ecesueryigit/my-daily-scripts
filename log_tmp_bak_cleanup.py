import os
import subprocess
import shutil


dizin_yolu = input("Bir dizin yolu girin: ")


if  not os.path.exists(dizin_yolu):

    os.makedirs(dizin_yolu)


for f in os.listdir(dizin_yolu):

    dosya_yolu= os.path.join(dizin_yolu, f)


    if os.path.isfile(dosya_yolu) and f.endswith((".log" , ".tmp" , ".bak")):

        os.remove(dosya_yolu)

        print(f"{dosya_yolu} dosyasi silindi.")



yedek_arsivi= "yedekler"

os.makedirs(yedek_arsivi , exist_ok= True)


os.path.join(dizin_yolu, yedek_arsivi )

yedek_adi= os.path.join(yedek_arsivi , "yedek")


shutil.make_archive(yedek_adi, "zip" , dizin_yolu)


disk_durumu= subprocess.run(["df", "-h" , dizin_yolu] , capture_output= True , text= True , check= True)

print(disk_durumu.stdout.strip())

