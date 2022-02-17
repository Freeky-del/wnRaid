from os import system
from colorama import Fore
import tools.WebhookDestroyer.utilities.spam as spam
import tools.WebhookDestroyer.utilities.webhook as webhook


def main():
    DeleteWebhook = input(Fore.RED + '[!]' + Fore.CYAN + 'Do you wanna delete the WebHook ? ')
    clear = system('cls')

    if DeleteWebhook == 'yes':
        webhook.hook.delete()
        print(Fore.GREEN + '[>]WebHook Deleted')
    
    if DeleteWebhook == 'no':
    # ModifyWebHook = input(Fore.CYAN + 'Do yo wanna modify the WebHook ? ')
    # clear = system('cls')
    
    # if ModifyWebHook == 'yes':
    #     Name = input('Insert a Name for WebHook Here: ')
    #     clear = system('cls')
    #     AvatarImage = input('Do you wanna change the avatar? ')
    #     clear = system('cls')
        
        # if AvatarImage == 'yes':
        #     with open('avatar\\avatar.png', 'rb') as f:
        #         img = base64.b64encode(f.read())
        #         avatar = bytearray(img)
        #     hook.modify(name = {Name}, avatar = avatar)
        #     print(Fore.GREEN + '[>]WebHook Modified succefully')
        
        # if AvatarImage == 'no':
        #     hook.modify(name = f"{Name}")
        #     print(Fore.GREEN + '[>]WebHook Modified succefully')

    # if ModifyWebHook == 'no':
        spam.main()