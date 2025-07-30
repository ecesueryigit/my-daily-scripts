import os
import subprocess

klasor_yolu= input("Klasör yolunu girin: ")

if os.path.isdir(klasor_yolu):

    try:

        sonuc= subprocess.run(
            ["ls" , klasor_yolu], capture_output=True , text= True , check= True)
        
        print("Output: " , sonuc.stdout)


        user= subprocess.run(
            ["whoami"] , capture_output=True , text=True , check= True)

        print("Kullanici: " , user.stdout.strip())


        date= subprocess.run(
            ["date"] , capture_output= True , text= True , check= True)

        print("Tarih: " , date.stdout.strip())

    
    except subprocess.CalledProcessError as e:

        print("Hata: " , e.stderr)

else:

    print("Klasör yolu bulunamadi.")