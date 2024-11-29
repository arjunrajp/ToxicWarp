import requests
import random
import requests
import json
import pyfiglet
import sys
import time
import os
import uuid
import webbrowser
import fake_useragent



Ab = '\033[1;92m'
aB = '\033[1;91m'
AB = '\033[1;96m'
aBbs = '\033[1;93m'
AbBs = '\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
ab = pyfiglet.figlet_format("TOXIC ARJUN")
print(a_bSa + ab)


def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)


to(
    f"\033[31;m Script Type>> \033[1;36mUnlimted Warp 1.1.1.1 Vpn \n\033[1;31m Telegram >>\033[1;33m@Toxicarjun\n\033[31;m Creator >>\033[1;33m@CDMAXX\n\033[31;m Tool Status >>\033[1;33mWorking\n\033[31;m Tool Value >>\033[1;33mPaid Script\n\033[31;m Time >>\033[1;33m24 Hours\n\033[31;m")
print('')
print('\033[32;m')
os.system('cls' if os.name == 'nt' else 'clear')
print('Unlimted Warp Free_)\n')
print ("[+] ABOUT SCRIPT:")
print ("[-] With this script, you can getting unlimited GB on Warp+.")
print ("[-] Version: 4.0.0")
print ("--------")
print ("[+] 𝐓𝐡𝐢𝐬 𝐒𝐜𝐫𝐢𝐩𝐭 𝐌𝐚𝐤𝐢𝐧𝐠 𝐁𝐲 𝐓𝐨𝐱𝐢𝐜 𝐀𝐫𝐣𝐮𝐧") 
print ("[-] SITE: agithub.io") 
print ("[-] TELEGRAM: @𝐩𝐫𝐢𝐯𝐚𝐭𝐞𝐚𝐫𝐣𝐮𝐧")
print ("--------")
referrer = input("[#] Enter the WARP+ ID:")
def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	

g = 0
b = 0
while True:
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("                  WARP-PLUS-CLOUDFLARE (script)" + "  𝐁𝐲 𝐓𝐨𝐱𝐢𝐜 𝐀𝐫𝐣𝐮𝐧")
		print("")
		animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
		for i in range(len(animation)):
			time.sleep(0.5)
			sys.stdout.write("\r[+] Preparing... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n[-] WORK ON ID: {referrer}")    
		print(f"[:)] {g} GB has been successfully added to your account.")
		print(f"[#] Total: {g} Good {b} Bad")
		print("[*] After 18 seconds, a new request will be sent.")
		time.sleep(18)
	else:
		b = b + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("                  WARP-PLUS-CLOUDFLARE (script)" + "  𝐁𝐲 𝐓𝐨𝐱𝐢𝐜 𝐀𝐫𝐣𝐮𝐧")
		print("")
		print("[:(] Error when connecting to server.")
		print(f"[#] Total: {g} Good {b} Bad")