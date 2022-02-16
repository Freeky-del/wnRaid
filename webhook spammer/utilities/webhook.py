from os import system
from time import sleep
import sys
from dhooks import Webhook
from colorama import Fore

def main():
    Webhook1 = input(Fore.CYAN + 'Webhook URL Here: ')

    if not Webhook1.__contains__('https://discord.com/api/webhooks/'):
        clear = system('cls')
        print(Fore.RED + '\n[!] Invalid URL!!')
        print(Fore.GREEN + '\nPlease restart the program')
        sleep(3)
        sys.exit()

    global hook
    hook = Webhook(Webhook1)
    clear = system('cls')