# -*- coding:utf-8 -*-
class Curso:

    def __init__(self, nome, cargaHoraria=0):
        self._nome = nome

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome        

# Criando a CLasse pessoas
class Pessoa:
    
    # Criando o dunder da classe Pessoas
    def __init__(self, nome):
        self._nome = nome

    # Criando o método get do atributo nome
    def getNome(self):
        return self._nome

    # Criando o método set do atributo nome
    def setNome(self, nome):
        self._nome = nome

# Criando a classe Professor herdando os atributos da classe Pessoa
class Professor(Pessoa):

    # Criando o dunder da classe Professor
    def __init__(self,nome, titulacaoMaxima, curso):
        Pessoa.__init__(self, nome)
        self._titulacaoMaxima = titulacaoMaxima

    # Criando o método get do atributo titulacaoMaxima
    def getTitulacaoMaxima(self):
        return self._titulacaoMaxima

    # Criando o método set do atributo titulacaoMaxima
    def setTitulacaoMaxima(self, titulacaoMaxima):
        self._titulacaoMaxima = titulacaoMaxima

    def getCurso(self):
        return self._curso

    def setCurso(self, curso):
        self._curso = curso

# Criando a classe Aluno herdando atributos da classe Pessoa
class Aluno(Pessoa):

    # Criando o dunder da classe Aluno
    def __init__(self, nome, matricula, situacao, notaProva1, notaProva2):
        Pessoa.__init__(self, nome)
        self._matricula = matricula
        self._situacao = situacao
        self._notaProva1 = notaProva1
        self._notaProva2 = notaProva2

    # Criando o método get do atributo matricula
    def getMatricula(self):
        return self._matricula

    # Criando o método set do atributo matricula
    def setMatricula(self, matricula):
        self._matricula = matricula

    # Criando o método get do atributo situacao
    def getSituacao(self):
        return self._situacao

    # Criando o método set do atributo situacao
    def setSituacao(self, situacao):
        self._situacao = situacao

    # Criando o método get do atributo notaProva1
    def getNotaProva1(self):
        return self._notaProva1

    # Criando o método set do atributo notaProva1
    def setNotaProva1(self, notaProva1):
        self._notaProva1 = notaProva1

    # Criando o método get do atributo notaProva2
    def getNotaProva2(self):
        return self._notaProva2

    # Criando o método set do atributo notaProva2
    def setNotaProva2(self, notaProva2):
        self._notaProva2 = notaProva2

    def calcularSituacao(self):
        return (self._notaProva1 + self._notaProva2) / 2

# Criando a classe AlunoEnsinoMedio
class AlunoEnsinoMedio(Aluno):

    # Criando o dunder da classe AlunoEnsinoMedio
    def __init__(self, nome, matricula, situacao, notaProva1, notaProva2):
        Aluno.__init__(self, nome, matricula, situacao, notaProva1, notaProva2)

    # Criando o método para calcular a situacao do aluno
    def verificarSituacao(self):
        if self.calcularSituacao() >= 6 :
            return "Aprovado"
        else:
            return "Reprovado"
    
# Criando a classe AlunoGraduacao herdando atributos da classe Aluno
class AlunoGraduacao(Aluno):

    # Criando o dunder da classe AlunoGraduacao
    def __init__(self, nome, matricula, situacao, notaProva1, notaProva2):
        Aluno.__init__(self, nome, matricula, situacao, notaProva1, notaProva2)

    # Criando um método para calcular a situacao do aluno
    def verificarSituacao(self):
        if self.calcularSituacao() >= 7 :
            return "Aprovado"
        else:
            return "Reprovado"

# Criando uma instancia do objeto AlunoEnsinoMedio e imprimindo o nome, matricula, e a situação do aluno
alunoEM1 = AlunoEnsinoMedio("Leandro", 1, "A calcular", 5, 7)
print("Aluno do Ensino Médio :")
print("Nome = " + alunoEM1.getNome())
print("Nº de matrícula = " + str(alunoEM1.getMatricula()))
print("Situação do aluno = " + alunoEM1.verificarSituacao())

# Criando uma instancia do objeto AlunoGraduacao e imprimindo o nome, matricula e situação do aluno
alunoGraducao = AlunoGraduacao("Cunha", 2, "A calcular", 5, 5)
print("Aluno de Graduação : ")
print("Nome = " + alunoGraducao.getNome())
print("Nº de matrícula = " + str(alunoGraducao.getMatricula()))
print("Situação do aluno = " + alunoGraducao.verificarSituacao())

# Criando uma instancia do objeto Professor e imprimindo o nome e a titulação máxima
professor = Professor("Magalhães", "Doutorado")
print("Professor :")
print("Nome = " + professor.getNome())
print("Titulação Máxima = " + professor.getTitulacaoMaxima())