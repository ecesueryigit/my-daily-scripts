import os
import subprocess

servis= input("Servis adini girin: ")

try:

    servis_cikti= subprocess.run(

        ["systemctl" , "is-active" , servis] , 
        
        capture_output= True, text= True , check= True)
    
    if servis_cikti.returncode ==0:

        if servis_cikti.stdout.strip().lower() == "Active":

            print(f" {servis} aktif durumda.")

        elif servis_cikti.stdout.strip().lower() == "Inactive":

            print(f"{servis} aktif değil.")

        else:

            print("Servis durumu: " , 
                  servis_cikti.stdout.strip().lower())

    
    elif servis_cikti.returncode ==1:

        print("Servis kontrolü sağlanamadi.")

    else:

        print("Hata oluştu: " , servis_cikti.stderr)

except subprocess.CalledProcessError as e:

    print("Komut satiri hatasi: " , str(e))