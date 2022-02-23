# -*- coding:utf-8 -*-
class Funcionario:
	"""docstring for Funcionário"""
	def __init__(self, nome, salarioBruto, totalAcrescimo, totalDesconto):
		self.nome = nome
		self._salarioBruto = salarioBruto
		self._totalAcrescimo = totalAcrescimo
		self._totalDesconto = totalDesconto
		self._salarioLiquido = ""

	# Métodos get/set do atributo NOME
	def getNome(self):
		return "Nome = " + self.nome

	def setNome(self):
		self.nome = nome

	# Métodos get/set do atributo SALÁRIO BRUTO
	def getSalarioBruto(self):
		return "Salário Bruto = R$" + str(self._salarioBruto)

	def setSalarioBruto(self):
		self._salarioBruto = salarioBruto

	# Métodos get/set do atributo TOTAL DE ACRÉSCIMOS
	def getTotalAcrescimo(self):
		return "Total de Acréscimos = R$" + str(self._totalAcrescimo)

	def setTotalAcrescimo(self):
		self._totalAcrescimo = totalAcrescimo

	# Métodos get/set do atributo  TOTAL DE DESCONTO
	def getTotalDesconto(self):
		return "Total de Desconto = R$" + str(self._totalDesconto)

	def setTotalDesconto(self):
		self._totalDesconto = totalDesconto

	# Método para calcular o SALÁRIO LÍQUIDO
	def calcularSalarioLiquido(self):
		self._salarioLiquido = (self._salarioBruto + self._totalAcrescimo) - self._totalDesconto
		return ("Salário Líquido = R$") + str(self._salarioLiquido)

#Instaciando um objeto da classe Funcionário
funcionario1 = Funcionario("Leandro", 2000.00, 500.00, 300.00)

print(funcionario1.getNome())
print(funcionario1.getSalarioBruto())
print(funcionario1.getTotalAcrescimo())
print(funcionario1.getTotalDesconto())
print(funcionario1.calcularSalarioLiquido())