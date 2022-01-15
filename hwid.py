import subprocess
import requests
import time
import sys
import os

hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r = requests.get("ลิงค์ PastBin ที่เก็บ HWID")

def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.1)

def Main_Program():
    if hwid in r.text:
        os.system('cls' if os.name == 'nt' else 'clear')
        printSlow("[*] Let Fun")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.1)
        #ใส่ฟังชั่นหลัก
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        printSlow("[!]  You Do Not Have Access To This Program")
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print("Your HWID [>>>]   " + hwid)
        print()
        print('[!] Enter To Exit')
        os.system('pause >NUL')
    sys.exit()

if __name__ == "__main__":
    Main_Program()