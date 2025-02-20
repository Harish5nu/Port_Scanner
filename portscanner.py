import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    ports_to_scan = [21, 22, 23, 25, 53, 80, 443, 3306, 8080]  # Common ports
    scan_ports(target_ip, ports_to_scan)
