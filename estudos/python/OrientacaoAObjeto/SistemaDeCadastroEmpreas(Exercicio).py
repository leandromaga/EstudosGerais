# -*- coding:utf-8 -*-
# Criando a classe Grupo
class Grupo:
    def __init__(self, nome, presidente, sede): # Dunder da classe Grupo
        self._nome = nome
        self._presidente = presidente
        self._sede = sede

    # Criando métodos get e set dos atributos da classe Grupo
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome
    
    def getPresidente(self):
        return self._presidente

    def setPresidente(self, presidente):
        self._presidente = presidente
    
    def getSede(self):
        return self._sede

    def setSede(self, sede):
        self._sede = sede

    # Método get para retornar o a escolaridade do presidente do grupo
    def getEscolaridadePresidente(self):
        return self._presidente.getEscolaridadeFuncionario()

# Criando a classe Pais
class Pais:
    def __init__(self, nome): # Dunder da classe Pais
        self._nome = nome

    # Criando métodos get e set dos atributos da classe Pais
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

# Criando a classe Estado
class Estado:
    def __init__(self, nome, pais): # Dunder da classe Estado
        self._nome = nome
        self._pais = pais

    # Criando métodos get e set dos atribulos da classe Estado
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome    

    def getPais(self):
        return self._pais

    def setPais(self, pais):
        self._pais = pais

    def getPaisEstado(self):
        return self._pais.getNome()

# Criando classe Cidade
class Cidade:
    def __init__(self, nome, estado): # Dunder da classe Cidade
        self._nome = nome
        self._estado = estado

    # Criando métodos get e set dos atributos da classe Cidade
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getEstado(self):
        return self._estado

    def setEstado(self, estado):
        self._estado = estado1

    def getPaisCidade(self):
        return self._estado.getPaisEstado()

# Criando a classe Filial
class Filial:
    def __init__(self, nome, cidade, empresa): # Dunder da classe Filial
        self._nome = nome
        self._cidade = cidade
        self._empresa = empresa

    # Criando métodos get e set dos atributos da classe Filial
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome 

    def getCidade(self):
        return self._cidade

    def setCidade(self, cidade):
        self._cidade = cidade

    def getEmpresa(self):
        return self._empresa
    
    def setEmpresa(self, empresa):
        self._empresa = empresa

    # Método para retornar o nome do diretor da empresa
    def getNomeDiretor(self):
        return self._empresa.getDiretor().getNome()

# Criando classe Funcionario
class Funcionario:
    def __init__(self, nome, escolaridade, departamento, filial): # Dunder da classe Funcionario
        self._nome = nome
        self._escolaridade = escolaridade
        self._departamento = departamento
        self._filial = filial

    # Criando métodos get e set da classe Funcionario
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome   

    def getEscolaridade(self):
        return self._escolaridade

    def setEscolaridade(self, escolaridade):
        self._escolaridade = escolaridade

    def getDepartamento(self):
        return self._departamento

    def setDepartamento(self, departamento):
        self._departamento = departamento

    def getFilial(self):
        return self._filial

    def setFilial(self, filial):
        self._filial = filial

    # Método para retornar a escolaridade do funcionários
    def getEscolaridadeFuncionario(self):
        return self._escolaridade.getNome()

    # Método para retornar o nome do Pais do funcionario de uma filial
    def getPaisFuncionario(self):
        return self._departamento.getEmpresa().getGrupo().getSede().getNome()

    # Método para retornar o estado de uma filial
    def getEstadoFilial(self):
        return self._filial.getCidade().getEstado().getNome()

# Criando classe Departamento
class Departamento:
    def __init__(self, nome, chefe, empresa): # Dunder da classe Departamento
        self._nome = nome
        self._chefe = chefe
        self._empresa = empresa

    # Métodos get e set dos atributos da classe Departamento
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome  

    def getChefe(self):
        return self._chefe

    def setChefe(self, chefe):
        self._chefe = chefe

    def getEmpresa(self):
        return self._empresa

    def setEmpresa(self, empresa):
        self._empresa = empresa

    # Método para retornar a escolaridade do chefe do departamento
    def getEscolaridadeChefe(self):
        return self._chefe.getEscolaridade().getNome()

    def getPaisDepartametno(self):
        return self._empresa.getPaisEmpresa()

# Criando a classe Empresa
class Empresa:
    def __init__(self, nome, grupo, diretor): # Dunder da classe Empresa
        self._nome = nome
        self._grupo = grupo
        self._diretor = diretor

    # Métodos get e set dos atributos da classe Empresa
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome  

    def getGrupo(self):
        return self._grupo

    def setGrupo(self, grupo):
        self._grupo = Grupo

    def getDiretor(self):
        return self._diretor

    def setDiretor(self, diretor):
        self._diretor = diretor

    def getPaisEmpresa(self):
        return self._grupo.getSede().getNome()

# Criando a classe Escolaridade
class Escolaridade:
    def __init__(self, nome): # Dunder da classe Escolaridade
        self._nome = nome

    # Métodos get e set dos atributos da classe Escolaridade
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome  

# Rever pais, estado, cidade, filial sobre as associações
pais1 = Pais("Brasil")
estado1 = Estado("Minas Gerais", pais1)
cidade1 = Cidade("Juiz Fora", estado1)
filial1 = Filial("Filial 1", cidade1, "") # inserir empresa
escolaridade1 = Escolaridade("Doutorado")
grupo1 = Grupo("Grupo 1", "", pais1) # inserir presidente
empresa1 = Empresa("Empresa 1", grupo1, "") # inserir diretor
funcionario1 = Funcionario("Leandro", escolaridade1, "", filial1) # inserir departamento
departamento1 = Departamento("Departamento 1", funcionario1, empresa1)

# Estâncias dos objetoss
filial1.setEmpresa(empresa1)
grupo1.setPresidente(funcionario1)
empresa1.setDiretor(funcionario1)
funcionario1.setDepartamento(departamento1)

# Respostas sem métodos adicionais
print("A escolaridade do presidente do grupo é : {}".format(grupo1.getPresidente().getEscolaridade().getNome()))
print("O país de alocação de um funcionário é : {}".format(funcionario1.getDepartamento().getEmpresa().getGrupo().getSede().getNome()))
print("O estado da filial que um funcionário coordena é : {}".format(funcionario1.getFilial().getCidade().getEstado().getNome()))
print("A escolaridade do chefe de um departamento é : {}".format(departamento1.getChefe().getEscolaridade().getNome()))
print("O nome do diretor da empresa de uma filial é : {}".format(filial1.getEmpresa().getDiretor().getNome()))
print("")
# Respostas com métodos adicionais
print("A escolaridade do presidente do grupo é : {}".format(grupo1.getEscolaridadePresidente()))
print("O país de alocação de um funcionário é : {}".format(funcionario1.getPaisFuncionario()))
print("O estado da filial que um funcionário coordena é : {}".format(funcionario1.getEstadoFilial()))
print("A escolaridade do chefe de um departamento é : {}".format(departamento1.getEscolaridadeChefe()))
print("O nome do diretor da empresa de uma filial é : {}".format(filial1.getNomeDiretor()))