from celula_atm import CelulaATM
import socket
import pickle
import time

class Emissor:
    @staticmethod
    def calcular_hec(vpi, vci, pt, clp):
        return (vpi + vci + pt + clp) % 256

    def enviar_celula(self, destino, vpi, vci, pt, clp, payload):
        hec = self.calcular_hec(vpi, vci, pt, clp)
        celula = CelulaATM(vpi, vci, pt, clp, hec, payload)
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(destino)
            s.send(pickle.dumps(celula))

if __name__ == "__main__":
    emissor = Emissor()
    destino = ('localhost', 65432)  # Endereço e porta do receptor
    
    dados_para_enviar = "Célula ATM 1: Informações importantes. Célula ATM 2: Dados de vídeo. Célula ATM 3: Pacote de voz em tempo real."
    tamanho_bloco = 48
    for i in range(0, len(dados_para_enviar), tamanho_bloco):
        bloco = dados_para_enviar[i:i + tamanho_bloco]
        emissor.enviar_celula(destino, 10, 20, 1, 0, bloco)
        time.sleep(5)

