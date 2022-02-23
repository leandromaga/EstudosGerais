from .Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        Pessoa.__init__(self, nome)
        self._cpf = cpf

    def getCpf(self):
        return self._cpf

    def setCpf(self, cpf):
        self._cpf = cpf