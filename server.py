#! python2

# Imports
import socket
import hashlib
import sys
from game import Game

# Informacoes do socket
HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

# Informacoes de login - comum
contaComum = hashlib.md5('user').hexdigest() # Conta do usuario
senhaComum = hashlib.md5('123').hexdigest() # Senha do usuario

# Informacoes de login - admin
contaAdmin = hashlib.md5('admin').hexdigest() # Conta do admin
senhaAdmin = hashlib.md5('124').hexdigest() # Senha do admin

# Mensagem que retornara para o usuario
feedback = ""

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
def sendMessage(message):
	try:
		con.send(message)
	except socket.timeout:
		print 'Falha ao enviar mensagem'

# Funcao responsavel por verificar se a senha funciona
def checkPassword(password, type):
	if (type == 1):
		if (password == senhaComum):
			sendMessage('Senha correta! Bem vindo Sylveon!')
			return True
		else:
			sendMessage('Senha incorreta! Finalizando...')
			return False
	else:
		if (password == senhaAdmin):
			sendMessage('Senha correta! Bem vindo usuario administrativo Vaporeon!')
			return True
		else:
			sendMessage('Senha incorreta! Finalizando...')
			return False
# Funcao responsavel pelo login
def checkLogin(con):
	msg = receiveMessage(con)
	if not msg: 
		return False
	if (msg == contaComum):
		sendMessage('Logando como usuario comum. Por favor digite sua senha: ')
		msg = receiveMessage(con)
		return checkPassword(msg, 1)
	if (msg == contaAdmin):
		sendMessage('Logando como administrador. Por favor digite sua senha: ')
		msg = receiveMessage(con)
		return checkPassword(msg, 2)
	else:
		sendMessage('Usuario nao encontrado. Finalizando conexao.')
		return False

# Dados da conexao
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

# Inicia a conexao
while True:
	con, cliente = tcp.accept()
	print 'Concetado por', cliente

	game = Game()
	gameRunning = True

	sendMessage('Bem vindo ao Moongrove! Digite o nome de usuario para continuar.')
	if (checkLogin(con)):
		while gameRunning:
			stepChoice = receiveMessage(con)
			if (gameRunning):
				gameRunning = game.execute(stepChoice)
				sendMessage(game.getMessage())
	print 'Finalizando conexao do cliente', cliente
	con.close()
	sys.exit()