from celula_atm import CelulaATM
import socket
import pickle

class Receptor:
    def processar_celula(self, celula):
        print("Recebendo", celula)
        # Aqui, você pode adicionar a lógica para processar a célula.

if __name__ == "__main__":
    while True:
        receptor = Receptor()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', 65432))  # Endereço e porta para escutar
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    celula = pickle.loads(data)
                    receptor.processar_celula(celula)
