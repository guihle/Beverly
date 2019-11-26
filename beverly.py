#!/usr/bin/python3
from googlesearch import search
import requests, argparse, random, dork

parser = argparse.ArgumentParser(description='SQLi Finder')
parser.add_argument('-p', type=str, help='Customized google Dork (optional), default=\"inurl:view_items.php?id=\"')
parser.add_argument('-n', type=int, help='Results quantity(optional, default=10)')
parser.add_argument('-r', action='store_true', help='Generate random list')
parser.add_argument('-d', action='store_true', help='Use random dork')
args = parser.parse_args()
par = args.p
numo = args.n
rand = args.r
d = args.d

print(" ____     ___ __ __    ___  ____   _      __ __     ")
print("|    \   /  _]  |  |  /  _]|    \ | |    |  |  |    ")
print("|  o  ) /  [_|  |  | /  [_ |  D  )| |    |  |  |    ")
print("|     ||    _]  |  ||    _]|    / | |___ |  ~  |    ")
print("|  O  ||   [_|  :  ||   [_ |    \ |     ||___, |    ")
print("|     ||     |\   / |     ||  .  \|     ||     |    ")
print("|_____||_____| \_/  |_____||__|\_||_____||____/     ")
print("                                                    ")

start = 0
num = 10
if numo:
    if numo >= 1 and numo <= 50:
        num = numo
    else:
        print("Number must be an integer between 1 and 50")
        quit()

if rand:
    start = random.randint(0,100)

print("Scanning for Vulnerable Web Pages, please hold...\n")
if not par:
    pes = "inurl:view_items.php?id="
else:
    pes = par


try:
    if d:
        pes = random.choice(dork.dork)
    for j in search(pes, tld="com", num=10, start=start ,stop=num, pause=60):
        if d:
            pes = random.choice(dork.dork)
        res = requests.get(j).content
        site = j + "'"
        res2 = requests.get(site).content
        if res != res2:
            print("\033[1;32;40m",j, " - LIKELY INJECTABLE")
        else:
            print("\033[1;31;40m",j, " - Unlikely Injectable")
except requests.exceptions.RequestException:
    pass
except KeyboardInterrupt:
    print("\nCtrl+C Pressed\nQuitting.")
    quit()
