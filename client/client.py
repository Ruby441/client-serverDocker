import socket
import time

# Attendi qualche secondo per assicurarti che il server sia pronto
time.sleep(2)

# Configurazione del client
SERVER_HOST = "172.17.0.2"  # Nome del servizio definito in docker-compose.yml
SERVER_PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Invia un messaggio al server
client_socket.sendall("Ciao server, sono il client!".encode())

# Riceve la risposta dal server
data = client_socket.recv(1024).decode()
print(f"Risposta del server: {data}")

# Chiude la connessione
client_socket.close()
