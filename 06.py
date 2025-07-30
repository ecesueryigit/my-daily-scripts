import os
import subprocess

klasor_path= input("Klasörü girin: ")

if os.path.isdir(klasor_path):

    try:

        loglar= os.listdir(klasor_path)

        for log in loglar:

            if log.endswith(".log"):
                
                yol= os.path.join(klasor_path, log)



                cikan= subprocess.run(
                        ["grep", "ERROR" , yol] , capture_output=True , text= True, check= True)


                if cikan.returncode ==0:

                    say= cikan.stdout.count("ERROR")
                    print("Error sayisi: " , say)

                elif cikan.returncode== 1:

                    print("Hiç error bulunamadi.")

                else:

                    print("Bir hata oluştu: " , cikan.stderr)   

            

    except subprocess.CalledProcessError as e:

        print("Error: " , str(e))                    

elif not os.path.isdir(klasor_path):

    print("Böyle bir klasör bulunamadi.")

else:

    print("Geçersiz işlem.")  