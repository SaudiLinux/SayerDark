#!/bin/bash
echo -e "\033[1;32m[*] Installing SayerDark v3.0...\033[0m"
sudo apt-get update && sudo apt-get install python3 python3-pip -y
pip3 install -r requirements.txt --break-system-packages
chmod +x SayerDark.py
echo -e "\033[1;34m[✔] Ready! Run: python3 SayerDark.py\033[0m"
