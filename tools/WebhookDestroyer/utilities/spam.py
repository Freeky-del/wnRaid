from os import system
from time import sleep
import sys
from colorama import Fore
import tools.WebhookDestroyer.utilities.webhook as webhook

def main():
    SelectWhatSpam = input(Fore.CYAN + 'Do you wanna spam an Image or a Message or both of them ? ')
    clear = system('cls')

    if SelectWhatSpam == 'Image' or SelectWhatSpam == 'image':
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

    if SelectWhatSpam == 'Message' or SelectWhatSpam == 'message':
        MessageToSpam = input(Fore.CYAN + 'What is the message which you want to spam ?  ')
        clear = system('cls')
        MentionEveryone = input('Do you wanna mention @everyone ?  ')
        clear = system('cls')
        MentionAnUser = input('Do you wanna mention a specific user? ')
        clear = system('cls')
                
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

                
                    

    if SelectWhatSpam == 'Both of them' or 'both of them':
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