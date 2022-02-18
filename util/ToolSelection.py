import webbrowser
from colorama import Fore
from pystyle import *
from time import sleep
from os import system
import sys
import tools.WebhookDestroyer.main as webhookDestroyer
import util.name as name
import tools.TokenBruteForcer.main as tkn

def main():
    sys.stdout.write("\x1b]2;wnRaid by echqq00 & Freeky-del\x07")

def main():
    ToolSelection = """
        [1] WebHook Destroyer

        [2] Token BruteForcer

        [3] Coming Soon...

        [99] Credits
    """

    print(Box.Lines(ToolSelection))
    print('\n\n')
    Selection = input(Fore.MAGENTA + '[>]Select a tool: ')

    if Selection == '1':
        webhookDestroyer.start()

    if Selection == '2':
        tkn.main()

    if Selection == '99':
        webbrowser.open('https://github.com/Freeky-del')
        webbrowser.open('https://github.com/Echqq00')
        print("Credits opened with success! Check out your browser")
        sleep(1)
        clear = system('cls')
        name.restart()
        main().Restart