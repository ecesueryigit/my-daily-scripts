import os
import shutil
import subprocess


print(os.getcwd())
os.mkdir("yedeklemeklasoru")
os.mkdir("hedefklasor")

kaynak= "."
hedef= os.path.join(kaynak, "hedef_klasor")

if not os.path.exists(kaynak):
    
    print("Kaynak dosya bulunamadi.")

else:
   
   os.mkdir(hedef)
   print("Hedef klasör oluşturuldu.")

shutil.copytree(kaynak, os.path.join(hedef, os.path.basename(kaynak)))
print("Kopyalama tamamlandi.")
 

for f in os.listdir("."):

    if os.path.isfile(f):

         print(f"Dosya: {f}")

    else:

         print(f"Klasör: {f}")



for f in os.listdir("."):

    if f.endswith(".log"):

        print(f"{f} bir log dosyasidir.")




for f in os.listdir("."):

    if os.path.isfile(f):

        print(f"Dosya adi: {f} , Boyut: {os.path.getsize(f) / 1024} KB ")