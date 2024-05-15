#!usr/bin/python3

import requests
import threading
import argparse
import os
import subprocess
import curses
import random
import time

TARGET = ""

LOGO = """

 ######   ####    ######   #### 
     ##  #    #       ##  #    #
     ##  #    #       ##  #    #
 #   ##  #    #  #    ##  #    #   
  ####    ####    #####    ####  

███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
   






"""

def attack(target, message):
    while True:
        try:
            response = requests.get(target)
            print("Request sent to:", target)
        except Exception as e:
            print("Failed to send request:", e)
        time.sleep(random.uniform(0.5, 2.0))  


def main(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    stdscr.addstr(0, (width // 2) - len(LOGO.split("\n")[0]) // 2, LOGO) 
    stdscr.addstr(stdscr.getmaxyx()[0] - 2, 0, "Use as setas para navegar e pressione Enter para selecionar uma opção")  
    stdscr.refresh()

    options = [
        ("Iniciar Ataque", "a"),
        ("Clonar Repositório", "c"),
        ("Instalar Dependências", "i"),
        ("Sair", "q")
    ]

    current_option = 0

    while True:
        key = stdscr.getch()  

        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(options) - 1:
            current_option += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:  
            if options[current_option][1] == "a":
               
                pass
            elif options[current_option][1] == "c":
            
                pass
            elif options[current_option][1] == "i":
          
                pass
            elif options[current_option][1] == "q":
                break

        stdscr.addstr(stdscr.lines // 2, (stdscr.cols // 2) - len(options[current_option][0]) // 2, options[current_option][0])
        stdscr.refresh()

curses.wrapper(main)
