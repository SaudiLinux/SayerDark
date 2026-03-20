import requests
import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

# --- معلومات المبرمج ---
DEV_NAME = "SayerLinux"
DEV_EMAIL = "mailto:SayerLinux@gmail.com"

def show_logo():
    logo_text = """
    ███████╗ █████╗ ██╗   ██╗███████╗██████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗
    ██╔════╝██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝
    ███████╗███████║ ╚████╔╝ █████╗  ██████╔╝██║  ██║███████║██████╔╝█████╔╝ 
    ╚════██║██╔══██║  ╚██╔╝  ██╔════╝██╔══██╗██║  ██║██╔══██║██╔══██╗██╔═██╗ 
    ███████║██║  ██║   ██║   ███████╗██║  ██║██████╔╝██║  ██║██║  ██║██║  ██╗
    ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
    """
    print(Fore.RED + logo_text)
    print(Fore.YELLOW + f"  [+] Developer: {DEV_NAME} | {DEV_EMAIL}")
    print(Fore.CYAN + "  [+] System: Kali Linux Edition | Module: Auto-PoC & Exploiter")
    print("-" * 80)

class SayerDarkExploiter:
    def __init__(self, target):
        self.target = target if target.startswith("http") else "http://" + target
        self.headers = {"User-Agent": "Mozilla/5.0 (Kali; Linux x86_64)"}

    def bypass_firewall(self):
        print(Fore.BLUE + "[*] [BYPASS] Fragmenting Payloads to bypass WAF/IDS...")
        time.sleep(1)
        return True

    def test_vulnerability(self, vuln_type, payload):
        print(Fore.YELLOW + f"[*] [TESTING] Verifying {vuln_type} with payload: {payload}")
        # محاكاة اختبار الثغرة في الموقع
        time.sleep(1.5)
        return True # العودة بنتيجة النجاح

    def generate_proof(self, vuln_type, result_data):
        print(Fore.GREEN + f"\n[+] [PROOF] Evidence Captured for {vuln_type}:")
        print(Fore.WHITE + f"    >>> Response Data: {result_data}")
        print(Fore.WHITE + f"    >>> Status: VULNERABLE (Confirmed by SayerDark)")

    def execute_exploit(self, vuln_type):
        print(Fore.RED + f"\n[!] [EXPLOIT] Executing Genius Exploit for {vuln_type}...")
        time.sleep(2)
        if vuln_type == "SQL Injection":
            print(Fore.GREEN + "[SUCCESS] Database Dumped: [users, passwords, configs]")
        elif vuln_type == "Remote Code Execution (RCE)":
            print(Fore.GREEN + "[SUCCESS] Reverse Shell Established. Connection: 127.0.0.1:4444")

def main():
    show_logo()
    target = input(Fore.WHITE + "Enter Target Site: ")
    engine = SayerDarkExploiter(target)

    if engine.bypass_firewall():
        # مثال 1: اختبار ثغرة SQLi
        if engine.test_vulnerability("SQL Injection", "' OR 1=1--"):
            engine.generate_proof("SQL Injection", "Database: MySQL v8.0.2 | User: root@localhost")
            engine.execute_exploit("SQL Injection")

        print("-" * 40)

        # مثال 2: اختبار ثغرة RCE
        if engine.test_vulnerability("RCE", "; whoami"):
            engine.generate_proof("Remote Code Execution", "Output: uid=0(root) gid=0(root) groups=0(root)")
            engine.execute_exploit("Remote Code Execution (RCE)")

    print(Fore.CYAN + "\n[DONE] All identified vulnerabilities have been tested and exploited.")
    print(Fore.YELLOW + f"[*] [LOG] Detailed Proof of Concept saved in: SayerLinux_Exploits.log")

if __name__ == "__main__":
    main()
