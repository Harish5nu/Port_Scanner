import socket
from datetime import datetime

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    if sock.connect_ex((target, port)) == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    sock.close()

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        scan_port(target, port)

    print(f"Scan completed in: {datetime.now() - start_time}")

target_ip = input("Enter IP to scan: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

scan_ports(target_ip, start_port, end_port)
