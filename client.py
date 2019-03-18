#! python2

# Imports
import socket
import hashlib
import sys

# Informacoes do socket
HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

# Dados da conexao
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

# Funcao responsavel por receber a mensagem
def receiveMessage(con):
	try:
		msg = con.recv (1024)
	except socket.timeout:
		print 'Falha ao enviar mensagem'
	
	if (msg):
		return msg
	else: 
		return False

# Funcao responsavel por enviar a mensagem
def sendMessage():
	try:
		msg = str(raw_input().encode("utf").strip())
		msg = hashlib.md5(msg).hexdigest()
		tcp.send(msg)
	except socket.timeout:
		print 'Falha ao enviar mensagem'

# Inicia a conexao
running = True
while running:
	try:
		response = tcp.recv(1024).decode()
		print response
	except socket.timeout:
		print "Conexao finalizada"
		running = False
	sendMessage()
tcp.close()
sys.exit()