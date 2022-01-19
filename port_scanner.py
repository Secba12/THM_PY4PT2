import sys, socket, pyfiglet

assci_banner = pyfiglet.figlet_format("TryHackMe\n PY$PY \n PortScanner")
print(assci_banner)

ip = '10.10.225.10'

open_ports = []

ports = range(1, 65535)

def probe_ports(ip, port, result=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        request = sock.connect_ex((ip, port))
        if request == 0:
            result = request
        sock.close()
    except Exception as e:
        pass
    return result

for port in ports:
    sys.stdout.flush()
    response = probe_ports(ip, port)
    if response == 0:
        open_ports.append(port)
        print(port)

if open_ports:
    print(f"Open ports {sorted(open_ports)}")
else:
    print('No open ports')