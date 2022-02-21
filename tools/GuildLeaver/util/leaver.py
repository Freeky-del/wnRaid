import os
import requests
from time import sleep
from colorama import Fore
import util.ToolSelection as ToolSelection
from pystyle import *

def leaver():
    token = open('tokens.txt').read().splitlines()

    if os.path.getsize('tokens.txt') == 0:
        print('No tokens avaible\n\nMake sure you have inserted token in tokens.txt')
        sleep(3)
        Write.Print("Restarting Program", Colors.green)
        sleep(2)
        ToolSelection.main()
    
    ID = input(Fore.MAGENTA + '[>]Insert Guild ID: ')

    with open('tokens.txt', 'r') as f:
            tokens = f.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

                }
        
                r = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/" + str(ID), headers = headers)
                if r.status_code == 200 or r.status_code == 204:
                    print(Fore.GREEN + "[>]Done")
                    sleep(2)
                else:
                    print(Fore.RED + f"[!]Didn't leave!\n\n[{r.status_code}] {r.text}")
                    sleep(2)