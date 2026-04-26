from scapy.all import sniff

def process_packet(packet):
    print(packet.summary())

if __name__ == "__main__":
    print("Starting packet capture...\n")
    sniff(prn=process_packet, count=20)
