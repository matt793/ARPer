# ARPer
What is ARPer?

ARPer is a mixture of Python and Bash scripting. This script helps a user easily setup a ARPposion attack. This is for Linux only.

## Instructions

First run the install.sh script of software dependences, and then change connection point/driver name to make script run.
    
You will then need to input your WiFi card into the prompt.

Find connection point by typing:

`iwconfig` for WiFi card/driver.

----

## Usage

Open the attack folder, then type `sudo ./ARPer.sh`

A coded Nmap scan will run (which will show defalt gateway, and a list of host targets)

If you know gateway and target: press `ctrl + C` 2x to skip Nmap scan. Wireshark will also open for network scanning.

First add gateway: will show up, type in your sub gateway ip.
then Add target: will show. Type in target ip, and the ARPposion attack will start.

Lastly start a Wireshark scan to watch the network traffic of the targeted ip.

type `ip.addr == <target ip>` into Wireshark search to monitor targeted traffic.
