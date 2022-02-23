from .Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome):
        Pessoa.__init__(self, nome)