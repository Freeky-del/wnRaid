from unicodedata import name
import pyautogui
from colorama import Fore, init
from pystyle import *

init ()

def main():
    name = """

        █     █░███▄    █  ██▀███   ▄▄▄       ██▓▓█████▄ 
        ▓█░ █ ░█░██ ▀█   █ ▓██ ▒ ██▒▒████▄    ▓██▒▒██▀ ██▌
        ▒█░ █ ░█▓██  ▀█ ██▒▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░██   █▌
        ░█░ █ ░█▓██▒  ▐▌██▒▒██▀▀█▄  ░██▄▄▄▄██ ░██░░▓█▄   ▌
        ░░██▒██▓▒██░   ▓██░░██▓ ▒██▒ ▓█   ▓██▒░██░░▒████▓ 
        ░ ▓░▒ ▒ ░ ▒░   ▒ ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓   ▒▒▓  ▒ 
        ▒ ░ ░ ░ ░░   ░ ▒░  ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒ 
        ░   ░    ░   ░ ░   ░░   ░   ░   ▒    ▒ ░ ░ ░  ░ 
            ░            ░    ░           ░  ░ ░     ░    
                                                ░      
                                                
    """

    Anime.Fade(Center.XCenter(name), Colors.purple_to_blue, Colorate.Vertical, interval = 0.050, enter = True)
    print(Fore.MAGENTA + Center.XCenter(name))

def restart():
    name = """

        █     █░███▄    █  ██▀███   ▄▄▄       ██▓▓█████▄ 
        ▓█░ █ ░█░██ ▀█   █ ▓██ ▒ ██▒▒████▄    ▓██▒▒██▀ ██▌
        ▒█░ █ ░█▓██  ▀█ ██▒▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░██   █▌
        ░█░ █ ░█▓██▒  ▐▌██▒▒██▀▀█▄  ░██▄▄▄▄██ ░██░░▓█▄   ▌
        ░░██▒██▓▒██░   ▓██░░██▓ ▒██▒ ▓█   ▓██▒░██░░▒████▓ 
        ░ ▓░▒ ▒ ░ ▒░   ▒ ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓   ▒▒▓  ▒ 
        ▒ ░ ░ ░ ░░   ░ ▒░  ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒ 
        ░   ░    ░   ░ ░   ░░   ░   ░   ▒    ▒ ░ ░ ░  ░ 
            ░            ░    ░           ░  ░ ░     ░    
                                                ░      
                                                
    """
    print(Fore.MAGENTA + Center.XCenter(name))