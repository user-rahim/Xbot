#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests, httplib, urllib
import socket
from platform import system
import os
import sys, time
import re
import threading
from multiprocessing.dummy import Pool
from colorama import Fore								
from colorama import Style								
from colorama import init												
init(autoreset=True)
fr  =   Fore.RED
fh  =   Fore.RED
fc  =   Fore.CYAN
fo  =   Fore.MAGENTA
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fbl =   Fore.BLUE
fg  =   Fore.GREEN											
sd  =   Style.DIM
fb  =   Fore.RESET
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT

user = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}

url = "http://www.zone-h.org/archive/notifier="
urll = "http://zone-h.org/archive/published=0"
url2 = "http://www.defacers.org/onhold!"
url4 = "http://www.defacers.org/gold!"
my_cook = {
	"ZHE" : "INPUT HERE",
	"PHPSESSID" : "INPUT HERE"
	}


def zonehh():
	print("""
	    |---| Grabb Sites From Zone-h |--|
		\033[91m[1] \033[95mGrabb Sites By Notifier
		\033[91m[2] \033[95mGrabb Sites By Onhold
		""")
	sec = int(raw_input("Choose Section: "))
	if sec == 1:
		notf = raw_input("\033[95mEnter notifier: \033[92m")

		for i in range(1, 51):
			dz = requests.get(url + notf +"/page=" + str(i), cookies=my_cook)
			dzz = dz.content
			print(url + notf +"/page=" + str(i))
			if '<html><body>-<script type="text/javascript"' in dzz:
				print("Change Cookies Please")
				sys.exit()
			elif '<input type="text" name="captcha" value=""><input type="submit">' in dzz:
				print("Entre Captcha In Zone-h From Ur Browser :/")
				sys.exit()	
			else:
				Hunt_urls = re.findall('<td>(.*)\n							</td>', dzz)
				if '/mirror/id/' in dzz:
					for xx in Hunt_urls:
						qqq = xx.replace('...','')
						print '    ['  + '*' + '] ' + qqq.split('/')[0]
						with open( notf + '.txt', 'a') as rr:
							rr.write("http://" + qqq.split('/')[0] + '\n')
				else:
					print("Grabb Sites Completed !!")
					sys.exit()
					
	elif sec == 2:
		print(":* __Grabb Sites By Onhold__ ^_^")
		for qwd in range(1, 51):
			rb = requests.get(urll + "/page=" + str(qwd) , cookies=my_cook)
			dzq = rb.content

			if '<html><body>-<script type="text/javascript"' in dzq:
				print("Change Cookies Plz")
				sys.exit()
				
			elif "captcha" in dzq:
				print("Entre captcha In Your Browser Of Site [zone-h.org]")
			else:
				Hunt_urlss = re.findall('<td>(.*)\n							</td>', dzq)
				for xxx in Hunt_urlss:
					qqqq = xxx.replace('...','')
					print '    ['  + '*' + '] ' + qqqq.split('/')[0]
					with open('onhold_zone.txt', 'a') as rrr:
						rrr.write("http://" + qqqq.split('/')[0] + '\n')
	else:
		print("Fuck You Men")

def defacers():
	print("""
		|---| Grabb Sites From Defacers.org |--|
			\033[91m[1] \033[95mGrabb Sites By Onhold
			\033[91m[2] \033[95mGrabb Sites By Archive
		""")
	sec = int(raw_input("Choose Section: "))
	if sec == 1:
		for i in range(1, 380):
			print("Page: "), str(i) + "\033[91m Waiting Grabbed Sites .....  <3"
			rb = requests.get(url2 + str(i),headers=user)
			okbb = rb.content
			domains = re.findall(r'title=".*" tar.?', okbb)
			for iii in domains:
				iii = iii.replace('" target="_blank" reel="nofollow">', "")
				iii = iii.replace('title="', "")
				iii = iii.replace('" targ', "")
				print("\033[95mhttp://" + iii + "/")
				with open("Onhold_defacer.txt", "a") as by:
					by.writelines("http://" + iii + "/")
					by.writelines("\n")
			print ("\t\t[+] Page Saved_"),str(i) +(" done [+]\n")
	elif sec == 2:
		for i in range(1, 25):
			print("Page: "), str(i) + " \033[91mWaiting Grabbed Sites Governement .....  <3"
			rb = requests.get(url4 + str(i),headers=user)
			okbb = rb.content
			domains = re.findall(r'title=".*" tar.?', okbb)
			for iii in domains:
				iii = iii.replace('" target="_blank" reel="nofollow">', "")
				iii = iii.replace('title="', "")
				iii = iii.replace('" targ', "")
				print("\033[95mhttp://" + iii + "/")
				with open("govSites_defacer.txt", "a") as by:
					by.writelines("http://" + iii + "/")
					by.writelines("\n")
			print ("\t\t[+] Page Saved_"),str(i) +(" done [+]\n")
	else:
		print("Fuck You Men 2")


def mirroirh():
	print("""
		   |---| Grabb Sites From Mirror-h.org |--|
			\033[91m[1] \033[95mGrabb Sites By Onhold
			\033[91m[2] \033[95mGrabb Sites By Auto_Notifier
		""")
	sec = int(raw_input("Choose Section: "))
	if sec == 1:
		url = "https://mirror-h.org/archive/page/"
		try:
			for pp in range(1, 40254):
				dz = requests.get(url + str(pp))
				dzz = dz.content
				qwd = re.findall(r'/zone/(.*)</a></td>', dzz)
				print(" \033[91m[*] Please Wait To Grabb Sites ...... Page: "), pp
				for ii in qwd:
					ii = ii.replace('<i class="icon-search"></i>', "")
					ii = ii.replace(ii[:10], "")
					ii = ii.replace("\r\n\r\n", "\r\n")
					ii = ii.strip()
					#iio = ii.replace('<i class="icon-search"></i>', "hhhhhhhhhhhhh")
					print("\033[95m" + ii)
					with open( 'onzeb_mirror.txt', 'a') as rr:
						rr.write(ii + '\n')
		except:
			pass
	elif sec == 2:
		url = "https://mirror-h.org/search/hacker/" 
		try:
			for ha in range(1, 2000):
				print("\033[91mWait To Grabb From Hacker: "), ha
				dz = requests.get(url + str(ha) + "/pages/1")
				dzz = dz.content
				qwd = re.findall(r'/pages/\d" title="Last"', dzz)
				for i in qwd:
					i = i.rstrip()
					sss = i.replace("/pages/","")
					ss = sss.replace('" title="Last"',"")
					ssf = int(ss) + 1
					for ii in range(1, ssf):
						print(" \033[91m[*] Please Wait To Grabb Sites ...... Page: "), ii
						dd = requests.get(url + str(ha) + "/pages/"+ str(ii))
						op = dd.content
						qwdd = re.findall(r'/zone/(.*)</a></td>', op)
						for idi in qwdd:
							idi = idi.replace('<i class="icon-search"></i>', "")
							idi = idi.replace(idi[:10], "")
							idi = idi.replace("\r\n\r\n", "\r\n")
							idi = idi.strip()
							#iio = ii.replace('<i class="icon-search"></i>', "hhhhhhhhhhhhh")
							print("\033[95m" + idi)
							with open( 'top_mirror.txt', 'a') as rr:
								rr.write(idi + '\n')
		except:
			pass


def overflowzone():
	print("""
		|---| Grabb Sites From overflowzone.com |--|
			\033[91m[1] \033[95mGrabb Sites By Onhold
			\033[91m[2] \033[95mGrabb Sites By AutoNotifier
		""")
	sec = int(raw_input("Choose Section: "))
	if sec == 1:
		url = "http://attacker.work/onhold/onhold/page/"
		dz = requests.get(url + "1")
		dzz = dz.content
		tn = re.findall(r'<a href="/onhold/page/(.*)" title="Last">', dzz)
		for ii in tn:
			qwd = ii.split('/')[-1]
			for ok in range(1, int(qwd)):
				okk = requests.get(url + str(ok))
				print("`\t\t\t" + url + str(ok))
				fel = okk.content
				okkk = re.findall(r'">http://(.*)</a></td>', fel)
				for iii in okkk:
					iii = iii.rstrip()
					print("\033[95mhttp://" + iii.split('/')[0])
					with open( 'onhold_attackerwork.txt', 'a') as rr:
						rr.write("http://" + iii.split('/')[0] + '\n')
	elif sec == 2:
		url = "http://attacker.work/archive/page/"
		dz = requests.get(url + "1")
		dzz = dz.content
		tn = re.findall(r'<a href="/archive/page/(.*)" title="Last">', dzz)
		for ii in tn:
			qwd = ii.split('/')[-1]
			for ok in range(1, int(qwd)):
				okk = requests.get(url + str(ok))
				print("`\t\t\t" + url + str(ok))
				fel = okk.content
				okkk = re.findall(r'">http://(.*)</a></td>', fel)
				for iii in okkk:
					iii = iii.rstrip()

					print("\033[95mhttp://" + iii.split('/')[0])
					with open( 'archive_attackerwork.txt', 'a') as rr:
						rr.write("http://" + iii.split('/')[0] + '\n')
	else:
		print("hhhhhhhh tnkt")
def bYPAS():
	exploit = ["/member/","/admin/login.php","/admin/panel.php","/admin/","/login.php","/admin.html","/admin.php","/admin-login.php"]
	try:
		q = raw_input('\033[96m Entre Liste Site: \033[90m ')
		q = open(q, 'r')
	except:
		print("\033[91mEntre List Sites -_- #Noob ")
		sys.exit()
	for lst in q:
		lst = lst.rstrip()
		print("\033[94m 	Wait Scaning ....... \033[94m"), lst
		for exploits in exploit:
			exploits.rstrip()
			try:
				if lst[:7] == "http://":
					lst = lst.replace("http://","")
				if lst[:8] == "https://":
					lst = lst.replace("https://", "")
				if lst[-1] == "/":
					lst = lst.replace("/","")
				socket.setdefaulttimeout(5)
				conn = httplib.HTTPConnection(lst)
				conn.request("POST", exploits)
				conn = conn.getresponse()
				htmlconn = conn.read()
				if conn.status == 200 and ('type="password"') in htmlconn:
					print("\033[92m [+] Admin Panel [+] ======\033[96m=======> \033[96m ") , lst + exploits
					with open("admin_panels.txt", "a") as by:
						by.writelines(lst + exploits + "\n")
				else:
					print("\033[91m [-] Not Found : [-]"),lst + exploits
			except:
				pass

def add_http():
	dz = raw_input("Entre List Site: ")
	dz = open(dz, "r")
	for i in dz:
		i = i.rstrip()
		print("http://"+i)
		with open( 'aziz.txt', 'a') as rr:
			rr.write("http://" + i + '\n')
	print("Text Saved !!")

def clearscrn():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
clearscrn()

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

def helper4():
	clearscrn()
	banner = """\033[94m"""
	print("")
	print("""
		\033[91m[1] \033[95mGrabb Sites  \033[92m From Zone-h.org   |  \033[91m[3] \033[95mGrabb Sites  \033[92m From mirror-h.org     |
		\033[91m[2] \033[95mGrabb Sites  \033[92m From Defacers.org |  \033[91m[4] \033[95mGrabb Sites  \033[92m From overflowzone.com |
		
		\033[91m[5] \033[95mGet Sites bypass With List [Bypass Finder]
		\033[91m[6] \033[95mMass Add (http://) To List ^_^
		\033[91m[7] \033[95mGrabber Sites From Bing :D
			""")		
	try:
		qq = int(raw_input("\033[91m[-] \033[90mroot@user~# \033[92mChoose Section !!\033[95m : \033[90m"))
		if qq == 1:
			clearscrn()
			print(banner)
			zonehh()
		if qq == 2:
			clearscrn()
			print(banner)
			defacers()
		if qq == 3:
			clearscrn()
			print(banner)
			mirroirh()
		if qq == 4:
			clearscrn()
			print(banner)
			overflowzone()
		if qq == 5:
			clearscrn()
			print(banner)
			bYPAS()
		if qq == 6:
			clearscrn()
			print(banner)
			add_http()
		if qq == 7:
			clearscrn()
			print(banner)
			binger()
		if qq == 8:
			clearscrn()
			print(banner)
			cms_detected()
		if qq == 9:
			clearscrn()
			print(banner)
			spotii()

	except:
		pass
helper4()