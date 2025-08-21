#НЕ ОБРАЩАЙТЕ ВНИМАНИЕ НА ТО ЧТО НЕКОТОРЫЕ ПЕРЕМЕННЫЕ ВЫДЕЛЕНЫ КРАСНЫМ ЦВЕТОМ, ВСЕ БУДЕТ РАБОТАТЬ КОРРЕКТНО

from scapy.all import *
import socket

BLOCKED_DOMAINS = [
    "web.max.ru",
    "max.ru",
    "vk.com",
    "download.max.ru",
    "trk.mail.ru",
    "ws-api.oneme.ru",
    "sdk-api.apptracer.ru"
]

FAKE_IP = "0.0.0.0"

def dns_spoof(packet):
    if packet.haslayer(DNSQR):
        qname = packet[DNSQR].qname.decode().rstrip(".")
        for domain in BLOCKED_DOMAINS:
            if domain in qname:
                print(f"[BLOCKED] {qname}")
                spoofed_pkt = IP(dst=packet[IP].src, src=packet[IP].dst)/\
                              UDP(dport=packet[UDP].sport, sport=53)/\
                              DNS(id=packet[DNS].id,
                                  qr=1, aa=1, qd=packet[DNS].qd,
                                  an=DNSRR(rrname=packet[DNS].qd.qname, ttl=60, rdata=FAKE_IP))
                send(spoofed_pkt, verbose=0)
                break

if __name__ == "__main__":
    print("Starting auto DNS blocker for hotspot...")
    sniff(filter="udp port 53", prn=dns_spoof)
