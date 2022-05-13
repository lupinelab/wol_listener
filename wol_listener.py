#!/usr/bin/env python

import argparse
import socket

parser = argparse.ArgumentParser(description='Listen for Wake-on-LAN Packets')
parser.add_argument("-p", "--port", type=int, nargs=1, help="Choose port to listen on")
args = parser.parse_args()


def wol_listener(port=9):
    host = ""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.bind((host, port))
        except PermissionError:
            print("Please run as elevated user")
            return
        print(f"Listening for Wake-on-LAN packets on port {port}:")
        while True:
            magic_packet = s.recv(1024).hex()
            raw_mac = magic_packet.strip("f")[0:12].upper()
            mac = ':'.join(raw_mac[i:i+2] for i in range(0, len(raw_mac), 2))
            print(mac)


if args.port:
    try:
        wol_listener(args.port[0])
    except KeyboardInterrupt:
        print("Stopped listening")
else:
    try:
        wol_listener()
    except KeyboardInterrupt:
        print("Stopped listening")