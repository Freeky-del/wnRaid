import json
from os import system
from turtle import clear
import requests
import time
from colorama import Fore
import tools.Spammer.util.name as name

def main():
    tokens = open('tokens.txt', 'r').read().splitlines()
    server = input(Fore.MAGENTA + 'Insert server id: ')
    channel = input(Fore.MAGENTA + 'Insert channel id: ')

    clear = system('cls')

    name.main()

    messages_count = input(f'{Fore.MAGENTA}How many messages do you wanna spam ? ')
    if not messages_count.rstrip().isdigit():
        print(f"{Fore.RED}[!]Insert number not a string")
        messages_count = input(f'{Fore.MAGENTA}How many messages do you wanna spam ? ')

    elif int(messages_count) <= 0:
        print(f"{Fore.RED}[!]Insert a valid number")
        messages_count = input(f'{Fore.MAGENTA}How many messages do you wanna spam ? ')

    message = input(Fore.MAGENTA + 'Insert a message: ')

    if len(message) == 0:
        print(f"{Fore.RED}[!]No empty message accept")
        messages_count = input(f'{Fore.MAGENTA}Insert a message: ')

    payload = {
        "content": message,
        "tts": False
    }

    url = "https://discord.com/api/v9/channels/" + channel + "/messages"

    print(f"{Fore.GREEN}Starting in...")

    time.sleep(1)

    print(f"{Fore.GREEN}3")

    time.sleep(1)

    print(f"{Fore.GREEN}2")

    time.sleep(1)

    print(f"{Fore.GREEN}1")

    time.sleep(1)

    print(f"{Fore.GREEN}Started")

    clear
    name.main()

    for i in range(int(messages_count)):
        for token in tokens:
            token = token.rstrip()

            header = {

                "access-control-allow-credentials": "true",
                "accept": "*/*",
                "path": "/api/v9/science",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "it-IT",
                "Authorization": token,
                "referer": "https://discord.com/channels/"+ server + "/" + channel ,
                "content-length": "0",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

            }

            r = requests.post(url, headers=header, json=payload)

            if r.status_code == 200:
                print(f"{Fore.GREEN}[>]Sent")

            if r.status_code == 429:
                ratelimit = json.loads(r.content)
                print(f"{Fore.YELLOW}[!]Ratelimit for {str(float(ratelimit['retry_after']))} seconds")
                time.sleep(float(ratelimit['retry_after']))
                
            if r.status_code == 404:
                print(Fore.RED + '[!]Channel Not Found')
                
            if r.status_code == 403:
                print(Fore.RED + f'[!]Missing Access\n[!]Check the token permissions {token}')

    # while True:
    #     for token in tokens:

    #         token = token.rstrip()

    #         header = {

    #         "access-control-allow-credentials": "true",
    #         "accept": "*/*",
    #         "path": "/api/v9/science",
    #         "accept-encoding": "gzip, deflate, br",
    #         "accept-language": "it-IT",
    #         "Authorization": token,
    #         "referer": "https://discord.com/channels/"+ server + "/" + channel ,
    #         "content-length": "0",
    #         "sec-fetch-dest": "empty",
    #         "sec-fetch-mode": "cors",
    #         "sec-fetch-site": "same-origin",
    #         "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
    #         "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
    #         "x-debug-options": "bugReporterEnabled",
    #         "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

    #         }
    #         r = requests.post(url, headers=header, json=payload)

    #         if r.status_code == '200':
    #             print(f"{Fore.GREEN}[>]Sent")

    #         if r.status_code == '429':
    #             ratelimit = json.loads(r.content)
    #             print(f"{Fore.YELLOW}[!]Ratelimit for {str(float(ratelimit['retry_after']))} seconds")
    #             time.sleep(str(float(ratelimit['retry_after'])))
                
    #         if r.status_code == '404':
    #             print(Fore.RED + '[!]Channel Not Found')
                
    #         if r.status_code == '403':
    #             print(Fore.RED + f'[!]Missing Access\n[!]Check the token permissions {token}')



