from os import system
from pystyle import *
from colorama import init, Fore
import pyautogui

def main():
    init()

    pyautogui.press('f11')

    clear = system('cls')
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

    name1 = """"
    
 █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀   ▓█████▄ ▓█████   ██████ ▄▄▄█████▓ ██▀███   ▒█████ ▓██   ██▓▓█████  ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒    ▒██▀ ██▌▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒▒██  ██▒▓█   ▀ ▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░    ░██   █▌▒███   ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒ ▒██ ██░▒███   ▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄    ░▓█▄   ▌▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░ ░ ▐██▓░▒▓█  ▄ ▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄   ░▒████▓ ░▒████▒▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░ ░ ██▒▓░░▒████▒░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒    ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░   ██▒▒▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░    ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░ ▓██ ░▒░  ░ ░  ░  ░▒ ░ ▒░
  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░     ░ ░  ░    ░   ░  ░  ░    ░        ░░   ░ ░ ░ ░ ▒  ▒ ▒ ░░     ░     ░░   ░ 
    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░         ░       ░  ░      ░              ░         ░ ░  ░ ░        ░  ░   ░     
                      ░                                      ░                                                 ░ ░                     

    """


    Anime.Fade(Center.Center(name), Colors.purple_to_blue, Colorate.Vertical, interval=0.050, enter=True)

    print(Fore.MAGENTA + Center.XCenter(name1))
