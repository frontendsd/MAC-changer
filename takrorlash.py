###########################################################################################################################################

#!/usr/bin/env python

import subprocess
import optparse
import re


def get_argements():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest = "new_mac", help="its new MAC address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error(["[-] Please specify an interface, use --help for more info."])
    elif not options.new_mac:
        parser.error(["[-] Please specify a new mac, use --help for more info."])

    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
        ifconfig_result = subprocess.check_output(
            ["ifconfig", interface]).decode()  # decode bytes-like object to string
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            print(f"Cannot find MAC address for interface '{interface}'")
            return None


options = get_argements()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))


change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was succesfully changed to" + current_mac)
else:
    print("[-] MAC address did not get changed")



###########################################################################################################################################



# #!/usr/bin/env python
#
# import scapy.all as scapy
#
# def scan(ip):
# 	arp_request = scapy.ARP()
# 	scapy.ls(scapy.ARP())
# 	print(arp_request.summary())
# scan("192.168.31.1/24")
