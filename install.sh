#!/bin/bash
green='\e[1;32m'
red='\e[1;31m'
echo "Please Wait... "
sleep 2
pkg install unzip -y
pkg install python2 -y
pip2 install requests
pip2 install Queue
pip2 install colorama
pip2 install parse
pip2 install system
ppm install Parallel-ForkManager && cpan -i Parallel::ForkManager
unzip Xbot.zip
echo "Please Wait... "
sleep 2
echo -e "${red}Done Install Module Now Runing Xbot :)\n"
ls
