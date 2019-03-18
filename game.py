#! python2

# Imports
import socket
import hashlib

class Game:
	currentStep = 1
	message = ""
	option1 = [1, ""]
	option2 = [1, ""]

	def showMessage(self):
		string = '------------- \n{}\n-------------\n'
		string += '\n[Digite 1]: {}'
		string += '\n[Digite 2]: {}'

		string.format(self.message, self.option1[1], self.option2[1])

		print string
		return True

	def execute(self, stepChoice):
		self.returnStep(stepChoice)

		#colocar fora da func
		switch = {1:self.enteredTheForest,2:self.leftTheForest,3:self.burnedTheForest}
		return switch[self.currentStep]()

	def returnStep(self, stepChoice):
		if (stepChoice == hashlib.md5('1').hexdigest()):
			self.currentStep = self.option1[0]
		elif(stepChoice == hashlib.md5('2').hexdigest()):
			self.currentStep = self.option2[0]
		else:
			string = '-------------\nOpcao invalida. Tente novamente!\n-------------'
			print string
			return False

	def enteredTheForest(self):
		self.message = 'Voce entrou na floresta'
		self.option1 = [2, 'Sair da floresta']
		self.option2 = [3, 'Queimar a floresta']

		return self.showMessage()

	def leftTheForest(self):
		self.message = 'Voce saiu da floresta'
		self.option1 = [1, 'Entrar na floresta']
		self.option2 = [3, 'Queimar a floresta']

		return self.showMessage()

	def burnedTheForest(self):
		self.message = 'Voce queimou a floresta'
		self.option1 = [1, 'Entrar na floresta']
		self.option2 = [3, 'Queimar a floresta']

		return self.showMessage()