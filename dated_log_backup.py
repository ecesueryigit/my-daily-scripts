import os
import subprocess
import shutil
import datetime

ana_klasor="logs"
os.makedirs(ana_klasor , exist_ok= True)

yedek_klasoru= "backup_logs"

os.makedirs(yedek_klasoru , exist_ok= True)


for dosya_adi in os.listdir(ana_klasor):

    tam_yol= os.path.join(ana_klasor , dosya_adi)

    if os.path.isfile(tam_yol) and dosya_adi.endswith(".log"):

        bugun= datetime.datetime.now().strftime("%Y-%m-%d")

        new_file_name= dosya_adi.replace(".log" , f"_{bugun}.log")

        hedef_yol= os.path.join(yedek_klasoru, new_file_name)

        shutil.copy2(tam_yol, hedef_yol)

        print(f"{dosya_adi} - {new_file_name} yedeklendi.")