import sys
from socket import socket,AF_INET,SOCK_STREAM

if len(sys.argv) < 4:
    print ("Not Enough Invalid request. Needs IP and 2 or more ports")
    sys.exit

host = sys.argv[1]
ports = sys.argv[2:]
def knocking(ports):
    for port in ports:
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(1)
        s.connect_ex((host,int(port)))
        s.close()
        print(f"Knocking on port {port}")

knocking(ports)