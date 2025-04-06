# simple_port_scanner.py

import socket

# Function to check if a port is open
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for the connection attempt
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open on {target}")
        sock.close()
    except socket.error:
        print(f"Couldn't connect to {target} on port {port}")

# Input from the user
target = input("Enter target IP address: ")
port = int(input("Enter port number to check: "))

# Scan the specified port
scan_port(target, port)
