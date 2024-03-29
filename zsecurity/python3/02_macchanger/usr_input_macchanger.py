#!/usr/bin/env python
import subprocess
import optparse

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the Mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new Mac address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please enter an interface , use --help for more info")
    elif not options.new_mac:
        parser.error("[-] please enter a mac adress, use --help for more info")
    return options
    
def change_mac(interface, new_mac):
    print("[+] changing the macadress for " + interface + " to " + new_mac)

    # subprocess.call("ifconfig "+interface+"down",shell=True)
    # subprocess.call("ifconfig"+interface+"hw ether "+new_mac,shell=True)
    # subprocess.call("ifconfig"+interface+"up",shell=True)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
options = get_argument()
change_mac(options.interface, options.new_mac)