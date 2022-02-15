from os import system
from msilib.schema import File
from time import sleep
from turtle import title
import pyautogui
from dhooks import Webhook
from io import BytesIO
from colorama import init, Fore, Back, Style
import requests
import sys

init()

clear = system('cls')

Webhook1 = input(Fore.CYAN + 'Webhook URL Here: ')

if not Webhook1.__contains__('https://discord.com/api/webhooks/'):
    clear = system('cls')
    print(Fore.RED + '\n[!] Invalid URL!!')
    sys.exit(Fore.GREEN + '\nPlease restart the program')

hook = Webhook(Webhook1)
clear = system('cls')

DeleteWebhook = input(Fore.RED + '[!]' + Fore.CYAN + 'Do you wanna delete the WebHook ? ')

if DeleteWebhook == 'yes':
    hook.delete()
    print(Fore.GREEN + '[>]WebHooke Deleted')

if DeleteWebhook == 'no':
    SelectWhatSpam = input(Fore.CYAN + 'Do you wanna spam an Image or a Message or both of them ? ')
    clear = system('cls')

    if SelectWhatSpam == 'Image' or SelectWhatSpam == 'image':
        print(Fore.RED + '[!]' + Fore.CYAN + 'Insert a discord image URL\n\nExample: https://cdn.discordapp.com/attachments/942836096126029827/943244337066705047/trasferimento.png')
            
        ImageToSpam = input('\n\nImage URL Here: ')

        # response = requests.get(ImageToSpam)   
        # file = File(BytesIO(response.content), name = 'wow.png')

        if not ImageToSpam.__contains__('https://cdn.discordapp.com/'):
            clear = system('cls')
            print(Fore.RED + '\n[!] Invalid URL!!')
            sys.exit(Fore.GREEN + '\nPlease restart the program')
                
        while True:
            hook.send(f"{ImageToSpam}")
            print(Fore.GREEN + '[>]Sent')

    elif SelectWhatSpam == 'Message' or SelectWhatSpam == 'message':
        MessageToSpam = input(Fore.CYAN + 'What is the message which you want to spam ?  ')
        clear = system('cls')
        MentionEveryone = input('Do you wanna mention @everyone ?  ')
        clear = system('cls')
        
        if MentionEveryone == 'yes':
            while True:
                hook.send(f"@everyone {MessageToSpam}")
                print(Fore.RED + '[>]Sent')
        if MentionEveryone == 'no':
            while True:
                hook.send(f"{MessageToSpam}")
                print(Fore.GREEN + '[>]Sent')

    elif SelectWhatSpam == 'Both of them' or 'both of them':
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
                hook.send(f"@everyone {MessageToSpam}\n{ImageToSpam}")
                print(Fore.GREEN + '[>]Sent')
        if MentionEveryone == 'no':
            while True:
                hook.send(f"{MessageToSpam}\n{ImageToSpam}")
                print(Fore.GREEN + '[>]Sent')