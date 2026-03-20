#!/bin/bash

# --- SayerDark Installer for Kali Linux ---
# Developer: SayerLinux | mailto:SayerLinux@gmail.com

# الألوان
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${RED}"
cat << "EOF"
   _____                      _____                __    
  / ___/ ____ _ __  __ ___   / __  \ ____ _ _____ / /__  
  \__ \ / __ `// / / // _ \ / / / // __ `// ___// //_/  
 ___/ // /_/ // /_/ //  __// /_/ // /_/ // /   / ,<     
/____/ \__,_/ \__, / \___//_____/ \__,_//_/   /_/|_|    
             /____/                                      
EOF
echo -e "${YELLOW}[*] Starting SayerDark Installation on Kali Linux...${NC}"

# 1. تحديث المستودعات وتثبيت المتطلبات الأساسية
echo -e "${GREEN}[+] Updating system and installing python3-pip...${NC}"
sudo apt update && sudo apt install python3 python3-pip -y

# 2. تثبيت مكتبات البايثون من ملف requirements.txt
if [ -f "requirements.txt" ]; then
    echo -e "${GREEN}[+] Installing Python dependencies...${NC}"
    pip3 install -r requirements.txt
else
    echo -e "${RED}[!] requirements.txt not found! Installing manually...${NC}"
    pip3 install requests urllib3 colorama pyfiglet
fi

# 3. جعل ملف الأداة قابلاً للتنفيذ
chmod +x SayerDark.py

# 4. إنشاء اختصار في النظام لتشغيل الأداة بكلمة واحدة
echo -e "${GREEN}[+] Creating system shortcut 'SayerDark'...${NC}"
sudo ln -sf "$(pwd)/SayerDark.py" /usr/local/bin/SayerDark

echo -e "${YELLOW}------------------------------------------------------------${NC}"
echo -e "${GREEN}[SUCCESS] SayerDark v3.0 has been installed successfully!${NC}"
echo -e "${YELLOW}[*] Developer: SayerLinux | Email: SayerLinux@gmail.com${NC}"
echo -e "${RED}[!] You can now start the tool from anywhere by typing: SayerDark${NC}"
echo -e "${YELLOW}------------------------------------------------------------${NC}"
