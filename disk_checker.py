import logging
import shutil

logger= logging.getLogger("disk_checker")

logger.setLevel(logging.DEBUG)


console_handler= logging.StreamHandler()
console_handler.setLevel(logging.INFO)



file_handler= logging.FileHandler("disk.log")
file_handler.setLevel(logging.ERROR)


formatter= logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(console_handler)



total, used , free = shutil.disk_usage("/")

free_gb= (free/ (1024**3))



if free_gb >5:

   logger.info("More than 5 GB of space")

   print(free_gb)

elif free_gb >2 :
   
   logger.warning("Less than 5 GB of space")

   print(free_gb)

else:
   
   logger.error("Less than 2 GB of space")

   print(free_gb)


