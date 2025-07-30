import os
import subprocess

klasor= input("Log dosyalarini bulmak istediğiniz klasörü girin: ")

if os.path.isdir(klasor):

    try:

        log_dosyalari= os.listdir(klasor)

        for log in log_dosyalari:

            if log.endswith(".log"):

                tam_yol= os.path.join(klasor, log)
                
                cikti= subprocess.run(
                    ["ls" , "-lh", tam_yol ] , capture_output=True , text= True , check= True)
                
                print("Output: " , cikti.stdout)


    except subprocess.CalledProcessError as e:

        print("Error: " , str(e))


elif not os.path.exists(klasor): 

    print("Böyle bir klasör bulunmuyor.")

else:

    print("Geçersiz işlem.")