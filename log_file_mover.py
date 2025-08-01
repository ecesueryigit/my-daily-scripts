import os
import subprocess
import shutil


log_kaynagi = "loglar_klasoru"

os.makedirs(log_kaynagi , exist_ok= True)

log_kaynagi_yolu= os.path.join(".", log_kaynagi)



log_hedefi = "hedef_klasor"

os.makedirs(log_hedefi , exist_ok= True)

log_hedefi_yolu = os.path.join("." , log_hedefi)



for item in os.listdir(log_kaynagi_yolu):

    log_yolu= os.path.join(log_kaynagi_yolu, item)


    if item.endswith(".log") and os.path.isfile(log_yolu):

        shutil.move(log_yolu, log_hedefi_yolu)


output= subprocess.run(["ls" , "-l" , log_hedefi_yolu ] ,
                        capture_output= True , text= True , check= True)

print(output.stdout.strip())