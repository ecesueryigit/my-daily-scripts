
import os
import subprocess
import logging
from datetime import datetime


log_file= "service_check.log"
logging.basicConfig( filename= log_file , 
                     filemode= "a" ,
                     force= "%(asctime)s - %(levelname)s - %(message)s" ,
                     level= logging.INFO
                     )


services= ["nginx" , "docker" , "sshd"]


def service_controller_and_restarter(service_name):

        
    try:

        is_active= subprocess.run(["systemctl" , "is-active" ,service_name ] , 
                                  capture_output= True , text= True , check= True )
        
        service_status= is_active.stdout.strip()
        
        logging.info(f"{service_name} Status: {service_status}")

        print(f"{service_name} Status: {service_status}")


        if service_status != "active" :
            
            logging.warning(f"{service_name} Inactive ,  restarting...")
            print(f"{service_name} Inactive, restarting...")

            restart= subprocess.run(["sudo" , "systemctl" , "restart" , service_name])


            if restart.returncode == 0 :

                logging.info(f"{service_name} is now active.")
                print(f"{service_name} is now active.")

            else:

                logging.error(f"{service_name} Error restarting : " , 
                              restart.stderr.strip())
                
                print(f"{service_name} Control error: " , 
                      restart.stderr.strip())
                
                
    except Exception as e:

        logging.error(f"{service_name} Control error.")
        print(f"{service_name} Control error.")

        
            
def main():

    logging.info("Service control started.")

    print("Service control started. ")


for srv in services:

    service_controller_and_restarter(srv)


logging.info("Completed")

print("Completed")


if __name__ == "__main__" :

    main()









