# -*- coding: utf-8 -*-
# Criando a classe Pessoa
class Pessoa:
    def __init__(self, nome, escolaridade, cidade): # Dunder da classe pessoa
        self._nome = nome
        self._escolaridade = escolaridade
        self._cidade = cidade

    # Métodos get e set dos atributos da classe Pessoa
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getEscolaridade(self):
        return self._escolaridade

    def setEscolaridade(self, escolaridade):
        self._escolaridade = escolaridade

    def getCidade(self):
        return self._cidade

    def setCidade(self, cidade):
        self._cidade = cidade

# Criando classe Aluno com herança da classe Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, escolaridade, cidade, curso):# dunder da classe pessoa
        Pessoa.__init__(self, nome, escolaridade, cidade)
        self._curso = curso

    # Métodos get e set dos atributos da classe Pessoa
    def getCurso(self):
        return self._curso

    def setCurso(self, curso):
        self._curso = curso

    def getEstadoNome(self):
        return self._cidade.getEstadoNome()

    def getEstadoEscola(self):
        return self._curso.getEstadoNome()

    def getCoordenadorCursoNome(self):
        return self._curso.getCoordenadorNome()

# Criando a classe Professor com herança da classe Pessoa
class Professor(Pessoa):
    def __init__(self, nome, escolaridade, cidade, curso):# Dunder da classe Professor
        Pessoa.__init__(self, nome, escolaridade, cidade)
        self._curso = curso
    
    # Métodos get e set dos atributos da classe Professor
    def getCurso(self):
        return self._curso

    def setCurso(self, curso):
        self._curso = curso

    def getEscolaridadeNome(self):
        return self._escolaridade.getNome()

    def getCidadeNome(self):
        return self._cidade.getNome()

    def getTipoEnsinoNome(self):
        return self._curso.getTipoEnsinoNome()

    def getDiretorEscolaNome(self):
        return self._curso.getDiretorEscolaNome()

    def getCoordenadorCursoNome(self):
        return self._curso.getCoordenadorNome()

# Criando a classe Escolaridade
class Escolaridade:
    def __init__(self, nome):# Dunder da classe escolaridade
        self._nome = nome

    # Métodos get e set dos atributos da classe Escolaridade
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

#Criando a classe TipoEnsino
class TipoEnsino:
    def __init__(self, nome):# Dunder da classe TipoEnsino
        self._nome = nome

    # Métodos get e set dos atributos da classe TipoEnsino
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

# Criando a classe Curso
class Curso:
    def __init__(self, nome, tipoEnsino, coordenador, escola):# Dunder da classe Curso
        self._nome = nome
        self._tipoEnsino = tipoEnsino
        self._coordenador = coordenador
        self._escola = escola

    # Métodos get e set dos atributos da classe Curso
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome 

    def getTipoEnsino(self):
        return self._tipoEnsino

    def setTipoEnsino(self, tipoEnsino):
        self._tipoEnsino = tipoEnsino

    def getCoordenador(self):
        return self._coordenador

    def setCoordenador(self, coordenador):
        self._coordenador = coordenador

    def getEscola(self):
        return self._escola

    def setEscola(self, escola):
        self._escola = escola

    def getEscolaridadeCoordenador(self):
        return self._coordenador.getEscolaridadeNome()

    def getEstadoNome(self):
        return self._escola.getEstadoNome()

    def getTipoEnsinoNome(self):
        return self._tipoEnsino.getNome()

    def getCoordenadorNome(self):
        return self._coordenador.getNome()
    
    def getDiretorEscolaNome(self):
        return self._escola.getDiretorNome()

# Criando a classe Estado
class Estado:
    def __init__(self, nome):# Dunder da classe Estado
        self._nome = nome

    # Métodos get e set dos atributos da classe Estado
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

#Criando a classe Cidade
class Cidade:
    def __init__(self, nome, estado):# Dunder da classe Cidade
        self._nome = nome
        self._estado = estado

    # Métodos get e set dos atributos da classe Cidade
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getEstado(self):
        return self._estado

    def setEstado(self, estado):
        self._estado = estado

    def getEstadoNome(self):
        return self._estado.getNome()

# Criando a classe Escola
class Escola:
    def __init__(self, nome, cidade, diretor):# Dunder da classe Escola
        self._nome = nome
        self._cidade = cidade
        self._diretor = diretor

    # Métodos get e set dos atributos da classe Escola
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome 

    def getCidade(self):
        return self._cidade

    def setCidade(self, cidade):
        self._cidade = cidade

    def getDiretor(self):
        return self._diretor

    def setDiretor(self, diretor):
        self._diretor = diretor

    def getEscolaridadeDiretor(self):
        return self._diretor.getEscolaridadeNome()

    def getEstadoNome(self):
        return self._cidade.getEstadoNome()

    def getDiretorNome(self):
        return self._diretor.getNome()

# Criando instancias das classes
estado01 = Estado("Minas Gerais")
cidade01 = Cidade("Juiz de Fora", estado01)
tipoEnsino01 = TipoEnsino("Superior")
escolaridade01 = Escolaridade("Ensino Médio Completo")
escolaridade02 = Escolaridade("Mestrado")
aluno01 = Aluno("Leandro", escolaridade01, cidade01, "")
professor01 = Professor("Marco", escolaridade02, cidade01, "")
professor02 = Professor("José", escolaridade02, cidade01, "") 
escola01 = Escola("UniAcademia", cidade01, professor02)
curso01 = Curso("Sistemas de Informação", tipoEnsino01, professor01, escola01)

aluno01.setCurso(curso01)
professor01.setCurso(curso01)
professor02.setCurso(curso01)

# Respostas
print("a) A escolariade de um professor é : {}".format(professor01.getEscolaridadeNome()))
print("b) A escolaridade do coordenador de um curso é : {}".format(curso01.getEscolaridadeCoordenador()))
print("c) A escolaridade do diretor de uma escola é : {}".format(escola01.getEscolaridadeDiretor()))
print("d) O estado de naturalidade de um aluno é : {}".format(aluno01.getEstadoNome()))
print("e) A cidade de nascimento de um professor é : {}".format(professor01.getCidadeNome()))
print("f) O estado em que um aludo estudo é : {}".format(aluno01.getEstadoEscola()))
print("g) O professor foi contratado para lecionar o tipo de ensino : {}".format(professor01.getTipoEnsinoNome()))
print("h) O coordenador do curso de um aluno é : {}".format(aluno01.getCoordenadorCursoNome()))
print("i) O diretor de um professor é : {}".format(professor01.getDiretorEscolaNome()))
print("j) O coordenador de um professor é : {}".format(professor02.getCoordenadorCursoNome()))