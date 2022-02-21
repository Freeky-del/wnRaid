from os import system
from time import sleep
import sys
from colorama import Fore
from pystyle import *
import tools.WebhookDestroyer.utilities.webhook as webhook

def main():
    WhatSpam = Box.Lines('What do you wnat to spam?\n\n[1]Image\n\n[2]Message\n\n[3]both of them')
    print(WhatSpam)
    SelectWhatSpam = input(Fore.CYAN + '\n\n[>]Choice: ')
    clear = system('cls')

    # if not (SelectWhatSpam == '1') or not (SelectWhatSpam == '2') or not (SelectWhatSpam == '3'):
    #     print(Fore.RED + '[!] ' + Fore.CYAN + 'Invalid Selection!')
    #     Write.Print('\nRestarting Program\nPlease Wait a few seconds', Colors.green)
    #     sleep(3)
    #     system('cls')
    #     system('py wnRaid.py')

    if SelectWhatSpam == '1':
            print(Fore.RED + '[!]' + Fore.CYAN + 'Insert a discord image URL\n\nExample: https://cdn.discordapp.com/attachments/942836096126029827/943244337066705047/trasferimento.png')
                
            ImageToSpam = input('\n\nImage URL Here: ')
            clear = system('cls')
            milidelay = input('Do you wanna a millisecond delay ? ')
            clear = system('cls')

            if milidelay == 'yes':
                delay1 = input('Insert a Delay in milliseconds (Ex: 50 or 10): ')
                while True:
                    webhook.hook.send(f"{ImageToSpam}")
                    print(Fore.GREEN + '[>]Sent')
                    sleep(int (delay1) / 10000)
            
            if milidelay == 'no':

                delay = input('Insert a Delay in seconds: ')
                # print(delay)
                # time.sleep(5)

                # response = requests.get(ImageToSpam)   
                # file = File(BytesIO(response.content), name = 'wow.png')

                if not ImageToSpam.__contains__('https://cdn.discordapp.com/'):
                    clear = system('cls')
                    print(Fore.RED + '\n[!] Invalid URL!!')
                    print(Fore.GREEN + '\nPlease restart the program')
                    sleep(3)
                    sys.exit()
                        
                while True:
                    webhook.hook.send(f"{ImageToSpam}")
                    print(Fore.GREEN + '[>]Sent')
                    sleep(int (delay))

    if SelectWhatSpam == '2':
        MessageToSpam = input(Fore.CYAN + 'What is the message which you want to spam ?  ')
        clear = system('cls')
        MentionEveryone = input('Do you wanna mention @everyone ?  ')
        clear = system('cls')
        MentionAnUser = input('Do you wanna mention a specific user? ')
        clear = system('cls')
        milidelay = input('Do you wanna a millisecond delay ? ')
        clear = system('cls')

        if milidelay == 'yes':
            delay1 = input('Insert a Delay in milliseconds (Ex: 50 or 10): ')
            while True:
                webhook.hook.send(f"{MessageToSpam}")
                print(Fore.GREEN + '[>]Sent')
                sleep(int (delay1) / 10000)
            
        if milidelay == 'no':

            delay = input('Insert a Delay in seconds: ')
            # print(delay)
            # time.sleep(5)

            # response = requests.get(ImageToSpam)   
            # file = File(BytesIO(response.content), name = 'wow.png')
                        
            while True:
                webhook.hook.send(f"{MessageToSpam}")
                print(Fore.GREEN + '[>]Sent')
                sleep(int (delay))
                
        if MentionEveryone == 'yes':
            while True:
                webhook.hook.send(f"@everyone {MessageToSpam}")
                print(Fore.GREEN + '[>]Sent')
        if MentionEveryone == 'no':
            if MentionAnUser == 'yes':
                UserID = input('Insert User ID Here: ')
                while True:
                    webhook.hook.send(f"{MessageToSpam} <@{UserID}>")
                    print(Fore.GREEN + '[>]Sent')
            if MentionAnUser == 'no':
                while True:
                    webhook.hook.send(f"{MessageToSpam}")
                    print(Fore.GREEN + '[>]Sent')

                
                    

    if SelectWhatSpam == '3':
        print(Fore.RED + '[!]' + Fore.CYAN + 'Insert a discord image URL\n\nExample: https://cdn.discordapp.com/attachments/942836096126029827/943244337066705047/trasferimento.png')
                    
        ImageToSpam = input('\n\nImage URL Here: ')

        # response = requests.get(ImageToSpam)   
        # file = File(BytesIO(response.content), name = 'wow.png')

        if not ImageToSpam.__contains__('https://cdn.discordapp.com/'):
            clear = system('cls')
            print(Fore.RED + '\n[!] Invalid URL!!')
            sys.exit(Fore.GREEN + '\nPlease restart the program')
                
        MessageToSpam = input('What is the message which you want to spam ?  ')
        clear = system('cls')
        MentionEveryone = input('Do you wanna mention @everyone ?  ')
        clear = system('cls')
                
        if MentionEveryone == 'yes':
            while True:
                webhook.hook.send(f"@everyone {MessageToSpam}\n{ImageToSpam}")
                print(Fore.GREEN + '[>]Sent')
        if MentionEveryone == 'no':
            while True:
                webhook.hook.send(f"{MessageToSpam}\n{ImageToSpam}")
                print(Fore.GREEN + '[>]Sent')