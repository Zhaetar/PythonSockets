#! python2

# Imports
import socket
import hashlib

class Game:
	# Qual zona atual ele esta
	currentStep = 1

	# Mensagem que sera exibida no cliente
	messageToClient = ""

	# Mensagem do evento
	message = ""

	# Opcao 1 do evento
	option1 = [1, ""]

	# Opcao 2 do evento
	option2 = [1, ""]

	def showMessage(self, exit):
		string = '------------- \n{}\n-------------\n'
		string += '\n[Digite 1]: {}'
		string += '\n[Digite 2]: {}'

		self.messageToClient = string.format(self.message, self.option1[1], self.option2[1])

		return not exit

	def execute(self, stepChoice):
		if (self.returnStep(stepChoice)):
			return True

		#colocar fora da func
		switch = {1:self.enteredTheForest,2:self.leftTheForest,3:self.burnedTheForest}
		return switch[self.currentStep]()

	def returnStep(self, stepChoice):
		if (stepChoice == hashlib.md5('1').hexdigest()):
			self.currentStep = self.option1[0]
		elif(stepChoice == hashlib.md5('2').hexdigest()):
			self.currentStep = self.option2[0]
		else:
			self.messageToClient = '-------------\nOpcao invalida. Tente novamente!\n-------------'
			return True

	def getMessage(self):
		return self.messageToClient

	def enteredTheForest(self):
		self.message = 'Voce entrou na floresta'
		self.option1 = [2, 'Sair da floresta']
		self.option2 = [3, 'Queimar a floresta']

		return self.showMessage(True)

	def leftTheForest(self):
		self.message = 'Voce saiu da floresta'
		self.option1 = [1, 'Entrar na floresta']
		self.option2 = [3, 'Queimar a floresta']

		return self.showMessage(False)

	def burnedTheForest(self):
		self.message = 'Voce queimou a floresta'
		self.option1 = [1, 'Entrar na floresta']
		self.option2 = [3, 'Queimar a floresta']

		return self.showMessage(True)