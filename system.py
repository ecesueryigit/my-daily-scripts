import subprocess
import os
import shutil
import logging


mem = subprocess.run(["free", "-m"] , 
                     capture_output= True , check= True , text= True)
print(mem.stdout)

cpu= subprocess.run(["uptime"] , 
                    capture_output= True , check= True , text= True)
print(cpu.stdout)


print("Current dir: " ,
       os.getcwd())
os.makedirs("logs" ,
             exist_ok= True)


disk_usage= shutil.disk_usage("/")

percent_free= disk_usage.free / disk_usage.total * 100

file_path= os.path.join("logs" , "app.log")


logging.basicConfig(filename= file_path,
                    level= logging.DEBUG,
                    format= "%(asctime)s - %(levelname)s - %(message)s")


if percent_free < 10 :
     logging.error(
          f"Free space is low {percent_free:.2f}")

else:
     logging.info(
          f"Free space is OK: %{percent_free:.2f}")
     

logging.info(
     "Memory:\n " + mem.stdout)

logging.info(
     "Cpu:\n " + cpu.stdout)