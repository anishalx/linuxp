#!/usr/bin/env python

import subprocess

# subprocess.call("ifconfig",shell=True)
# subprocess.call("ifconfig wlan0 down",shell=True)
# subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55",shell=True)
# subprocess.call("ifconfig wlan0 up",shell=True)
# subprocess.call("ifconfig wlan0",shell=True)

# for automatic change the mac address of 5 layers

subprocess.call("ifconfig",shell=True)
subprocess.call("ifconfig wlan0 down",shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55",shell=True)
subprocess.call("macchanger -e wlan0",shell=True)
subprocess.call("macchanger -e wlan0",shell=True)
subprocess.call("macchanger -e wlan0",shell=True)
subprocess.call("macchanger -e wlan0",shell=True)
subprocess.call("macchanger -e wlan0",shell=True)
subprocess.call("ifconfig wlan0 up",shell=True)
subprocess.call("ifconfig wlan0",shell=True)