# Usa Python come immagine di base
FROM python:3.13

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file server.py nel container
COPY server.py .

# Espone la porta 5000 per il server
EXPOSE 5000

# Avvia il server
CMD ["python", "server.py"]
