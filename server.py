import socket

Host = socket.gethostbyname(socket.gethostname())
Port = 6390

#création du socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((Host, Port))
socket.listen()
#le Script s'arrête jusqu'à une connexion

client, ip = socket.accept()
print("le client d'ip",ip,"s'est connecté")

while True:
    requete_client = client.recv(400)
    requete_client = requete_client.decode('utf-8')
    print(requete_client)
    if not requete_client: #si on perd la connexion
        print("connexion perdu")
        break
    msg = input("-->")
    msg = msg.encode("utf-8")
    client.send(msg)

client.close
socket.close()