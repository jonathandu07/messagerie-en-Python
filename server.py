import socket
from threading import Thread

def Send(socket):
    while True:
        msg = input()
        msg = msg.encode('utf-8')
        socket.send(msg)
def Reception(socket):
    while True:
        requete_server = socket.recv(500)
        requete_server = requete_server.decode("utf-8")
        print(requete_server)
Host = socket.gethostbyname(socket.gethostname())
Port = 6390

#création du socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((Host, Port))
socket.listen()
#le Script s'arrête jusqu'à une connexion

#Création du socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((Host,Port))

envoi = Thread(target=Send,args=[socket])
recep = Thread(target=Reception,args=[socket])

envoi.start()
recep.start()