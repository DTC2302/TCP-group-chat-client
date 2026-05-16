import socket
import threading
import os
import select

def msg(client):
    while True:
        msg = input()
        client.send(msg.encode())
        if (msg=='exit'):
            break

def recieve(client):
    while True:
        if (select.select([client], [], [])[0]):
            msg = client.recv(1024).decode()
            print(msg)
    

if (os.path.isfile("settings.txt")):
    try:
        with open("settings.txt", "r") as f:
            lines = f.read().split('\n')
            IP = lines[0].split(':')[-1]
            port = int(lines[1].split(':')[-1])
    except:
        print(f"Your settings .txt may be set up wrong, please make sure it follows this format \nIP:x.x.x.x \nPort:xxx")
else:
    print("There is no settings.txt please create a file 'settings.txt' in the running directory with the format: \nIP:x.x.x.x \nPort:xxx")
    exit()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((IP, port))
print(client.recv(1024).decode(),end="")
client.send(input().encode())
send = threading.Thread(target=msg, args=(client,))
recv = threading.Thread(target=recieve, args=(client,), daemon=True)
send.start()
recv.start()