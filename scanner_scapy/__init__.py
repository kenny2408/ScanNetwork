from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp


def main():
    ip = input('Ingresa la dirección IP:')

    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    print('Dispositivos encontrados en la red:')
    for sent, received in result:
        print(f'IP: {received.psrc} - MAC: {received.hwsrc}')


if __name__ == '__main__':
    main()
