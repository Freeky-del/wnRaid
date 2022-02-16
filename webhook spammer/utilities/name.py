from os import system
from msilib.schema import File
from pystyle import *
from colorama import init, Fore, Back, Style

def main():
    init()

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


    Anime.Fade(Center.Center(name), Colors.purple_to_blue, Colorate.Vertical, interval=0.050, enter=True)

    print(Fore.MAGENTA + Center.XCenter(name))