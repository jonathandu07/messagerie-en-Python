import socket

from server import requete_client

Host = socket.gethostbyname(socket.gethostname())
Port = 6391

#création du socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.connect((Host, Port))

while True:
    msg = input('-->')
    msg = msg.encode('utf-8')
    socket.send(msg)

    requete_server = socket.recv(400)
    requete_server = requete_server.decode('utf-8')
    print (requete_server)