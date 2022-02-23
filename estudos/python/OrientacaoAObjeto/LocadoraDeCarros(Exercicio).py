class Cliente:

    def __init__(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

class Veiculo:

    def __init__(self, placa, valor):
        self._placa = placa
        self._valor = valor
        self._alugado = False
        self._historico = []

    def alugar(self, cliente, dias):
        if (self._alugado == True):
            return "Veiculo de placa {} não disponível para aluguel".format(self._placa)
        else:
            self._alugado = True
            self._historico.append("Veiculo placa {} alugado pelo cliente {} no valor de R$ {}".format(self._placa, cliente.getNome(), self.calcularAluguel(dias)))
            return "Aluguel confirmado para o veículo de placa {}".format(self._placa)

    def devolver(self):
        if (self._alugado == False):
            return "Veiculo de placa {} não estava alugado".format(self._placa)
        else:
            self._alugado = False
            self._historico.append("Veiculo placa {} devolvido".format(self._placa))
            return "Devolução realizada para o veículo de placa {}".format(self._placa)

    def listarHistorico(self):
        print("\nHistórico do veículo de placa {}".format(self._placa))
        for historico in self._historico:
            print(historico)
        print("\n")

class Carro(Veiculo):

    def __init__(self, modelo, placa, valor):
        Veiculo.__init__(self, placa, valor)
        self._modelo = modelo

    def calcularAluguel(self, dias):
        return self._valor * dias

class Moto(Veiculo):

    def __init__(self, placa, valor):
        Veiculo.__init__(self, placa, valor)

    def calcularAluguel(self, dias):
        if dias >= 30:
            return self._valor * dias * 1.1
        else:
            return self._valor * dias * 1.2


cliente1 = Cliente("Marco")
cliente2 = Cliente("Antonio")

carro1 = Carro("Celta", "ABC123", 100)
carro2 = Carro("Uno", "XYZ123", 80)
moto1 = Moto("MOT123", 40)
moto2 = Moto("MOT234", 50)

print(carro1.alugar(cliente1, 10))
print(carro1.alugar(cliente1, 10))
print(carro1.devolver())
print(carro1.alugar(cliente2, 15))
carro1.listarHistorico()

print(carro2.devolver())

print(moto1.alugar(cliente1, 20))
print(moto1.devolver())
print(moto1.alugar(cliente2, 30))
moto1.listarHistorico()


