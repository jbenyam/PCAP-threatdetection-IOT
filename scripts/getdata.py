# python script that downloads all folders and files hosted at this url (http://205.174.165.80/IOTDataset/CIC_IOT_Dataset2023/Dataset/) and 
# stores the files and folder to this project directory (/home/jbenyam/threatdetection/dataset).
import os

# Specify the target directory where the folders will be created
target_directory = '/home/jbenyam/threatdetection/dataset/csv'

# List of folder names as seen in the image
folders = [
    "Benign_Final", "BrowserHijacking", "CommandInjection",
    "DDoS-ACK_Fragmentation", "DDoS-HTTP_Flood", "DDoS-ICMP_Flood",
    "DDoS-ICMP_Fragmentation", "DDoS-PSHACK_FLOOD", "DDoS-RSTFINFLOOD",
    "DDoS-SYN_Flood", "DDoS-SlowLoris", "DDoS-SynonymousIP_Flood", "DNS_Spoofing",
    "DictionaryBruteForce", "DoS-HTTP_Flood", "DoS-SYN_Flood", "DoS-TCP_Flood",
    "DoS-UDP_Flood", "DoS-UDP_Fragmentation", "MITM-ArpSpoofing", "Mirai-greeth_flood",
    "Mirai-greip_flood", "Mirai-udpplain", "Recon-HostDiscovery", "Recon-OSScan",
    "Recon-PingSweep", "Recon-PortScan", "SqlInjection", "Uploading_Attack", 
    "VulnerabilityScan", "XSS"
]

# Create each folder in the target directory
for folder in folders:
    folder_path = os.path.join(target_directory, folder)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created: {folder_path}")

print("All folders created successfully.")

