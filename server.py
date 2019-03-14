import socket
HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
contaComum = hash('user')
contaAdmin = hash('admin')
senhaComum = hash('batatinha')
senhaAdmin = hash('chocolate')
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

def receiveMessage(con):
	msg = con.recv (1024)
	return int (msg)

def checkPassword(password, type):
	if (type == 1):
		if (password == senhaComum):
			print 'Senha correta! Bem vindo Sylveon'
			return True
		else:
			print 'Senha incorreta! Finalizando...'
			return False
	else:
		if (password == senhaAdmin):
			print 'Senha incorreta! Bem vindo Vaporeon!'
			return True
		else:
			print 'Senha incorreta! Finalizando...'
			return False

def checkLogin(con):
	msg = receiveMessage(con)
	if not msg: 
		return False
	msg = int (msg)
	if (msg == contaComum):
		print 'Logando como usuario comum. Por favor digite sua senha: '
		msg = receiveMessage(con)
		return checkPassword(msg, 1)
	if (msg == contaAdmin):
		print 'Logando como administrador/ Por favor digite sua senha: '
		msg = receiveMessage(con)
		return checkPassword(msg, 2)
	else:
		print 'Usuario nao encontrado. Finalizando conexao.'
		return False

while True:
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    conexao = True
    while conexao:
    	conexao = checkLogin(con)   
    print 'Finalizando conexao do cliente', cliente
    con.close()