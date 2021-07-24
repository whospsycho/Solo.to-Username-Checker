import cloudscraper
import os
from threading import Thread
import time
from colorama import init,Fore
init()
os.system("title Psycho's Solo.to Username Checker")

cwd = os.path.dirname(os.path.realpath(__file__))

os.remove('available.txt')
names = open(fr'{cwd}\usernames.txt', 'r').read().splitlines()

scraper = cloudscraper.create_scraper()


def check_name(name):
    r = scraper.get(f"https://solo.to/{name}").text

    if f"@{name}" in r:
        print(f'{Fore.RED}[UNAVAILABLE] {name}')
    else:
        print(f'{Fore.GREEN}[AVAILABLE] {name}')
        with open('available.txt', 'a') as f:
                f.write(name + '\n')
        

threads = []
for name in names:
    threads.append(Thread(target=check_name, args=[name]))
for t in threads:
    t.start()
    time.sleep(0.01)
for t in threads:
    t.join()



input('Press ENTER to continue...')