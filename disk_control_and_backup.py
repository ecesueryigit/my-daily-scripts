import os
import shutil
import subprocess
import logging



print("Current dir: " , os.getcwd())
os.makedirs("backup" , exist_ok= True)


with open("test.txt" , "w") as f :
    f.write("Hello Backup")



backup= shutil.copy("test.txt" , "backup/test_backup.txt" )

logging.basicConfig(filename= "app.log" , 
                    level= logging.DEBUG ,
                    format = "%(asctime)s - %(levelname)s - %(message)s")

disk_usage= shutil.disk_usage("/")

percent_used = disk_usage.used / disk_usage.total * 100

if percent_used > 90 :

    logging.error(f"Disk occupancy is too high ! %{percent_used:.2f}")

elif percent_used > 80 :

    logging.warning(f"Disk full warning  %{percent_used:.2f}")

else:

    print(f"Disk status normal %{percent_used:.2f}")


result= subprocess.run(["ls" ,"-l", "backup"] , capture_output= True , check= True , text= True)
print(result.stdout)