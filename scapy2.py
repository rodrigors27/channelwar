#!/usr/bin/python3.5

import threading
import os, time
import random
from scapy.all import *

def hopper(iface):
    n = 1
    stop_hopper = False
    while not stop_hopper:
        time.sleep(0.50)
        os.system('iwconfig %s channel %d' % (iface, n))
        print("Current Channel %d" % (n))
        dig = int(random.random() * 12)
        if dig != 0 and dig != n:
            n = dig



F_bssids = []    # Found BSSIDs
def findSSID(pkt):
    if pkt.haslayer(Dot11Beacon):
       if pkt.getlayer(Dot11).addr2 not in F_bssids:
           F_bssids.append(pkt.getlayer(Dot11).addr2)
           ssid = pkt.getlayer(Dot11Elt).info
           print ("Network Detected: %s" % (ssid))

if __name__ == "__main__":
    interface = "wlan1mon"
    thread = threading.Thread(target=hopper, args=('wlan1mon', ), name="hopper")
    thread.daemon = True
    thread.start()

    sniff(iface=interface, prn=findSSID)
