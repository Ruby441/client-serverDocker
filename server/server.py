import socket

# Configurazione del server
HOST = "0.0.0.0"  # Accetta connessioni da qualsiasi indirizzo
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server in ascolto su {HOST}:{PORT}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connessione accettata da {addr}")
    
    # Riceve dati dal client
    data = client_socket.recv(1024).decode()
    print(f"Messaggio ricevuto: {data}")
    
    # Risponde al client
    client_socket.sendall("Ciao dal server!".encode())

    # Chiude la connessione
    client_socket.close()
