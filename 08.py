import os
import subprocess

klasorum= os.listdir(".")

try:

    for line in klasorum:

        if os.path.isfile(line):

            if line.endswith(".py"):

                dosya_yolu= os.path.join(".", line)

                sonucu= subprocess.run(["grep" , "-e" , "^import" , "-e" ,"^from" , dosya_yolu] ,
                                        capture_output= True, text= True , check= False)
                

                if sonucu.returncode == 0:

                    print("Modül içeren satirlar: " , sonucu.stdout.strip())

                elif sonucu.returncode == 1:

                    print("Modül bulunamadi.")

                else:

                    print("Hata: " , sonucu.stderr)


except subprocess.CalledProcessError as e:

    print("Komut satiri hatasi: " , str(e))