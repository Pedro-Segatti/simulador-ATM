import socket
import random

server_address = ('192.168.0.108', 12345)
cell_size = 53  # Tamanho da célula ATM em bytes

# VPI e VCI -> número de conexão virtual e identificador do caminho virtual
# Payload Type (PT) -> tipo de informação na célula (3 bits)
vc_mapping = {
    (0, 0, 0): 1,  # VPI=0, VCI=0, PT=0 mapeado para porta de saída 1
    (0, 1, 1): 2,
    (1, 0, 2): 3, 
    (1, 1, 0): 4, 
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)
print("Servidor ATM está aguardando conexões...")

def encaminhar_celula(vpi, vci, pt, data):
    key = (vpi, vci, pt)
    if key in vc_mapping:
        porta_saida = vc_mapping[key]
        print(f"Célula com VPI {vpi}, VCI {vci}, PT {pt} encaminhada para a porta de saída {porta_saida}.")
        return porta_saida, data
    else:
        print(f"Combinação VPI/VCI/PT não reconhecida: VPI {vpi}, VCI {vci}, PT {pt}. Descartando célula.")
        return None, None

while True:
    data, client_address = server_socket.recvfrom(cell_size)

    # Analisa o VPI, VCI e PT da célula para determinar o caminho ao qual a célula recebida pertence
    vpi = int.from_bytes(data[:2], byteorder='big')
    vci = int.from_bytes(data[2:4], byteorder='big')
    pt = (data[4] & 0b111)

    encaminhar_celula(vpi, vci, pt, data)
    break