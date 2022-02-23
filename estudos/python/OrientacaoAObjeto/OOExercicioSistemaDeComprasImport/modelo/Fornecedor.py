from .Pessoa import Pessoa

class Fornecedor(Pessoa):
    def __init__(self, nome, cnpj):
        Pessoa.__init__(self, nome)
        self._cnpj = cnpj

    def getCnpj(self):
        return self._cnpj

    def setCnphj(self, cnpj):
        self._cnpj = cnpj