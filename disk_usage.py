import logging
import shutil

file= "disk_monitor.log"

logging.basicConfig(filename= file,
                    filemode="a",
                    level= logging.DEBUG,
                    format= "%(asctime)s - %(levelname)s - %(message)s")

total , used , free = shutil.disk_usage("/")

free_gb= free / (1024**3)


if free_gb< 1 :

    logging.debug(f"Total space: {total / (1024**3):.2f} GB , \
                  Used space: {used / (1024**3): 2f} GB")


    logging.error("Error: Less than 1 GB of space ")

    logging.critical("Critical system failure: Disk almost full")


elif free_gb< 2 :
 
    logging.debug(f"Total space: {total / (1024**3):.2f} GB , \
                  Used space: {used / (1024**3): 2f} GB")

    logging.warning("Less than 2 GB of space ")

else :

    logging.debug(f"Total space: {total / (1024**3):.2f} GB , \
                  Used space: {used / (1024**3): 2f} GB")

    logging.info("System is operating normally ")



logging.debug(f"Total space: {total / (1024**3):.2f} GB , \
              Used space: {used / (1024**3): 2f} GB")


