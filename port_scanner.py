import socket
from datetime import datetime

def scan_port(host, port):
    try:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)

        result = scanner.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open.")
        else:
            print(f"Port {port} is closed.")
        scanner.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")    
    except socket.error:
        print("Couldn't connect to server.")

print("Python Port Scanner")
print(f"scanning started at: {datetime.now()}")

host = input("Enter the host to scan: ")

try:
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    for port in range(start_port, end_port + 1):
        scan_port(host, port)
except ValueError:
    print("Please enter valid port numbers.")