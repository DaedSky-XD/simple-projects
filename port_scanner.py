import socket

def clean_target(target: str):
    target = target.strip()
    if target.startswith("https://"):
        target = target.replace("https://", '').strip()

    elif target.startswith("http://"):
        target = target.replace("http://", '').strip()

    return target


def scan_port(target: str, port: int):
    try:
        sk = socket.socket()
        sk.settimeout(0.5)
        target = clean_target(target)
        sk.connect((target, port))
        try:
            service = sk.recv(1024)
            service = service.decode().removesuffix('\n')
            print(f"[+] port {port} is open : running {service}")
        except:
            print(f"[+] port {port} is open")

    except:
        pass


def scan_target(target: str, start_port: int = 70, stop_port: int = 100):
    if ',' in target:
        targets = target.split(',')
        for target in targets:
            print(f"[+] scanning {target.strip()}")

            for port in range(start_port, stop_port):
                scan_port(target, port)

    else:
        print(f"[+] scanning {target.strip()}")

        for port in range(start_port, stop_port):
            scan_port(target, port)


if __name__ == '__main__':
    target = input("[*] enter target/s to scan: ")
    start, end = input("[+] enter start port and end port: (use comma to seperate): ").split(',')
    scan_target(target=target)
