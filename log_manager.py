import os
import subprocess



os.makedirs("my_logs" , exist_ok= True)




log_dosyalar= ["touch" , "log1.txt", "log2.txt", "log3.txt"]

for dosya in log_dosyalar:

    dosya_yolu= os.path.join("my_logs" , dosya)
    subprocess.run(["touch" , dosya_yolu])



date= subprocess.run(["date"] , capture_output= True , text= True , check= True )

tarih= date.stdout.strip()



for dosya in log_dosyalar:

    with open(dosya_yolu , "a") as f:

        f.write(tarih + "\n")            



print("my_logs klasöründeki dosyalar: ")
for file in os.listdir("my_logs"):
   print("-" , file)