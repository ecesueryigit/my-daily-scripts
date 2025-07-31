import os
import subprocess
import shutil
from datetime import datetime

source_folder= "kaynakklasor"

os.makedirs(source_folder , exist_ok= True)

kaynak_yolu= os.path.join("." , source_folder)


backup_base_folder= "yedekdizini"

if not os.path.exists(backup_base_folder):

    os.makedirs(backup_base_folder , exist_ok= True)
    print("Backup dizini oluşturuldu.")

    yedek_yolu= os.path.join(".", backup_base_folder)


time= datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

proje_backup_name= f"proje_backup{time}" 

backup_folder= os.path.join(yedek_yolu, proje_backup_name )

os.makedirs(backup_folder)


try:

    shutil.copytree(kaynak_yolu,backup_folder)

    print(f"Klasör başariyla yedeklendi: {backup_folder}")

except Exception as e:

    print("Hata oluştu: " , e)
    exit(1)