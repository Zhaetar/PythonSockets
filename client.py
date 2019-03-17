#! python2

# Imports
import socket
import hashlib

# Informacoes do socket
HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

# Dados da conexao
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

msg = str(raw_input().encode("utf").strip())
# Inicia a conexao
while msg <> '\x18':
	msg = hashlib.md5(msg).hexdigest()
	tcp.send(msg)
	msg = raw_input()
tcp.close()