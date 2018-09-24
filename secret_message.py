import os
import random

def encrypt():
    file_directory1 = os.listdir(r"C:\IPND\alphabet")
    os.chdir(r"C:\IPND\alphabet")
    for entry in file_directory1:
        number = str(random.randint(1,9000))
        os.rename(entry, (number+ entry))
    
def decrypt():
    file_directory = os.listdir(r"C:\IPND\alphabet")
    os.chdir(r"C:\IPND\alphabet")
    for entry in file_directory:
        os.rename(entry, entry.translate(None, "0123456789"))
        
encrypt()
#decrypt()
