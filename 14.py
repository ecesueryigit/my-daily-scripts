import os
import subprocess
import shutil
import datetime

service= input("Servis adini girin: ")


service_status= subprocess.run(["systemctl" , "status" , service] , 
                                capture_output= True , text=True )


#servis kontrolü

if service_status.stdout.strip().returncode != 0 :

    log_klasoru= "logs"

    os.makedirs(log_klasoru , exist_ok= True)

    log_yolu= os.path.join(".", log_klasoru)


    #date

    date= datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


    #servis çalışmıyor

    with open(os.path.join(log_yolu , "servis.txt" , "w")) as f:

        f.write(f" {service} servisi çalişmiyor. Zaman: {date}")


    #yedekler için klasör

    yedek_klasoru= "yedek_klasor"

    os.makedirs(yedek_klasoru , exist_ok= True)

    yedek_yolu= os.path.join(log_yolu , yedek_klasoru)

    
    #log dosyası oluştur

    ornek_log= os.path.join(log_yolu , "ornek.log")


    with open(ornek_log , "w") as f:

        print("Bu bir log dosyasidir.")


    #log dosyasını yedekle
    copy= shutil.copy2(ornek_log, yedek_yolu)

    print("Log dosyasi kopyalandi.")
    

