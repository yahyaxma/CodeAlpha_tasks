from scapy.all import sniff, IP

def process_packet(packet):

    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto
        
        
        p_name = "Other"
        if proto == 6:
            p_name = "TCP"
        elif proto == 17:
            p_name = "UDP"
        elif proto == 1:
            p_name = "ICMP"
            
        print(f"[{p_name}] {src} -> {dst}")        
        
      
print("--- SNIFFER Active pn eth0 ---")
print("--- Press Ctrl+C to stop ---")


sniff(iface="eth0", prn=process_packet, store=False)
        
        
