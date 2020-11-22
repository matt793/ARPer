# ARPer
What is ARPer?

ARPer is a mixture of Python and Bash scripting. This script helps a user easily setup a ARPposion attack. This is for Linux only.

## Instructions

First run the install.sh script of software dependences, and then change connection point/driver name to make script run.

You also might need to turn all .py and .sh files into a exicutable by typing `chmod 755 <file name>`.
    
You will then need to input your WiFi card into the prompt.

Find connection point by typing:

`iwconfig` for WiFi card/driver.

You may need to change WiFi card name from wlan0 to the name of your device by changing the code python code. 
Go to ARPposion.py and change line 18. Delete wlan0 to the name of your device.

----

## Usage

Open the attack folder, then type `sudo ./ARPer.sh`

A coded Nmap scan will run (which will show defalt gateway, and a list of host targets)

If you know gateway and target: press `ctrl + C` 2x to skip Nmap scan. Wireshark will also open for network scanning.

First add gateway: will show up, type in your sub gateway ip.
then Add target: will show. Type in target ip, and the ARPposion attack will start.

Lastly start a Wireshark scan to watch the network traffic of the targeted ip.

type `ip.addr == <target ip>` into Wireshark search to monitor targeted traffic.
