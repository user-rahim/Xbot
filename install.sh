#!/bin/bash
green='\e[1;32m'
red='\e[1;31m'
#Header
ulang='y'
while [ $ulang == 'y' ]
do
echo "Please Wait... "
sleep 2
pkg install unzip -y
pkg install python2 -y
pip2 install requests
pip2 install Queue
pip2 install colorama
pip2 install parse
pip2 install system
unzip BoT.zip
echo "Please Wait... "
sleep 2
echo -e "${red}Done Install Module Now Runing Comand python2.py To Run AutoExploit\n"
ls
fi
echo -n -e "\e[1;31mNext Or Exit? (Select y/n): "
read ulang
done
clear
