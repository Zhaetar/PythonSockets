#! python2

# Informacoes do socket
import socket
HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

# Dados da conexao
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

# Inicia a conexao
msg = hash(raw_input())
while msg <> '\x18':
    tcp.send(str(msg))
    msg = raw_input()
tcp.close()