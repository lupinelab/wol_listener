import socket

def wol_listener():
    HOST = ""
    WAL_PORT = 9
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, WAL_PORT))
        while True:
            magic_packet = s.recv(1024).hex()
            #print(magic_packet)
            raw_mac = magic_packet.strip("f")[0:12].upper()
            mac = ':'.join(raw_mac[i:i+2] for i in range(0, len(raw_mac), 2))
            print(mac)

wol_listener()