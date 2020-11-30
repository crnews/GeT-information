from colorama import Fore
import requests as req
from time import sleep
print(Fore.RED+"""

 _        __                           _   _                     _                                              _
(_)      / _|                         | | (_)                   | |                                            | |
 _ _ __ | |_ ___  _ __ _ __ ___   __ _| |_ _  ___  _ __    _ __ | |__   ___  _ __   ___   _ __  _   _ _ __ ___ | |__   ___ _ __
| | '_ \|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \  | '_ \| '_ \ / _ \| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| | | | | || (_) | |  | | | | | | (_| | |_| | (_) | | | | | |_) | | | | (_) | | | |  __/ | | | | |_| | | | | | | |_) |  __/ |
|_|_| |_|_| \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_| | .__/|_| |_|\___/|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|
                                                          | |
                                                          |_|

coding by mobin-dan
site:crnews.ir    """)
number = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MobinDan"+Fore.BLUE+"~"+Fore.WHITE+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
num2 =input("Country code:")
print(Fore.LIGHTGREEN_EX+"╆╰target:╆╰"+num2+number)
print("")
print("Data collection....")
print("   □□□□□ 0%")
sleep(2)
print("   ■□□□□ 20%")
sleep(2)
print("   ■■□□□ 40%")
sleep(2)
print("   ■■■□□ 60%")
sleep(2)
print("   ■■■■□ 80%")
sleep(2)
print("   ■■■■■ 100%")
print("")
sleep(1)
print("-"*30)
Mobin_dan=req.get("https://phonenumbervalidation.apifex.com/api/v1/validate?phonenumber=%2B"+num2+"%20"+number).text
print(Fore.RED+Mobin_dan)
print("-"*30)
except:
        print("NOT FIND:(")
