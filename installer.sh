#!/bin/bash
# SayerDark v3.0 - Auto Installer Script
# Developer: SayerLinux

# الألوان للتنسيق
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}--------------------------------------------------${NC}"
echo -e "${GREEN}🛡️ SayerDark v3.0 - The Ultimate Hacking AI Edition${NC}"
echo -e "${BLUE}--------------------------------------------------${NC}"

# التحقق من صلاحيات الـ root
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}[!] يرجى تشغيل السكربت باستخدام sudo${NC}"
   exit 1
fi

echo -e "${BLUE}[*] تحديث النظام وتثبيت المكونات الضرورية...${NC}"
apt-get update -y
apt-get install python3 python3-pip -y

# تثبيت المكتبات
if [ -f "requirements.txt" ]; then
    echo -e "${BLUE}[*] تثبيت المكتبات من requirements.txt...${NC}"
    pip3 install -r requirements.txt --break-system-packages
else
    echo -e "${RED}[!] ملف requirements.txt غير موجود!${NC}"
    exit 1
fi

# إعطاء صلاحية التشغيل للملف الرئيسي
chmod +x SayerDark.py

echo -e "${GREEN}[✔] تم التثبيت بنجاح! يمكنك الآن تشغيل الأداة.${NC}"
echo -e "${BLUE}الأمر: python3 SayerDark.py${NC}"
