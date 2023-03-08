import nmap


def main():
    ip = input('Ingresa la dirección IP: ')

    nm = nmap.PortScanner()
    nm.scan(hosts=ip, arguments='-n .sP')

    print('Dispositivos encontrados en la red:')
    for host in nm.all_hosts():
        if nm[host]['status']['state'] == 'up':
            print(f"IP: {host} - MAC: {nm[host]['addresses']['mac']}")


if __name__ == '__main__':
    main()
