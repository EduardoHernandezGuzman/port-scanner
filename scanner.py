import socket

def scan_ports(target, start_port, end_port):
    open_ports = []
    print(f"Escaneando puertos de {start_port} a {end_port} en {target}...")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        print(f"Conectando al puerto {port}...")
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)

        sock.close()

    return open_ports

def get_service_name(port):
    try:
        service = socket.getservbyport(port)
        return service
    except:
        return "Unknown"

def main():
    target = input("Ingrese la dirección IP o el hostname: ")
    start_port = int(input("Ingrese el puerto de inicio: "))
    end_port = int(input("Ingrese el puerto de fin: "))

    print(f"Escaneando puertos en {target}...")

    open_ports = scan_ports(target, start_port, end_port)

    if len(open_ports) == 0:
        print("No se encontraron puertos abiertos.")
    else:
        print("Puertos abiertos:")
        for port in open_ports:
            service = get_service_name(port)
            print(f"Puerto {port}: {service}")

if __name__ == "__main__":
    main()
