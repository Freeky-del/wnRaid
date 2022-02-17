from os import system
import sys
from colorama import Fore
from pystyle import *
import tools.WebhookDestroyer.main as webhookDestroyer

def main():
    ToolSelection = """
        [1] WebHook Destroyer

        [2] Coming Soon...
    """

    print(Box.Lines(ToolSelection))
    print('\n\n')
    Selection = input(Fore.MAGENTA + '[>]Select a tool: ')

    if Selection == '1':
        webhookDestroyer.start()