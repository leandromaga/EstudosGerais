# -*- coding: utf-8 -*-
class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf):
        Pessoa.__init__(self, nome)
        self._cpf = cpf

    def getCpf(self):
        return self._cpf

    def setCpf(self, cpf):
        self._cpf = cpf

class Hospital(Pessoa):
    def __init__(self, nome, cnpj):
        Pessoa.__init__(self, nome)
        self._cnpj = cnpj

    def getCnpj(self):
        return self._cnpj

    def setCnpj(self, cnpj):
        self._cnpj = cnpj

    def getMedicoChefe(self):
        return self._medicoChefe

    def setMedicoChefe(self, medicoChefe):
        self._medicoChefe = medicoChefe

    def getMedicoChefeEspecialidade(self):
        return self._medicoChefe.getEspecialidade().getNome()

class Paciente(PessoaFisica):
    def __init__(self, nome, cpf):
        PessoaFisica.__init__(self, nome, cpf)

    def getMedicoAtende(self):
        return self._medicoAtende

    def setMedicoAtende(self, medicoAtende):
        self._medicoAtende = medicoAtende

    def getNomeMedicoAtende(self):
        return self._medicoAtende.getNome()

class Medico(PessoaFisica):
    def __init__(self, nome, cpf, especialidade, hospital):
        PessoaFisica.__init__(self, nome, cpf)
        self._especialidade = especialidade
        self._hospital = hospital

    def getEspecialidade(self):
        return self._especialidade

    def setEspecialidade(self, especialidade):
        self._especialidade = especialidade

    def getHospital(self):
        return self._hospital

    def setHospital(self, hospital):
        self._hospital = hospital

    def getNomeHospital(self):
        return self._hospital.getNome()

    def getNomeEspecialidade(self):
        return self._especialidade.getNome()

class Especialidade:
    def __init__(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

class Cirurgia:
    def __init__(self, nome, paciente, medico, dataCirurgia):
        self._nome = nome
        self._paciente = paciente
        self._medico = medico
        self._dataCirurgia = dataCirurgia

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getPaciente(self):
        return self._paciente
    
    def setPaciente(self, paciente):
        self._paciente = paciente

    def getMedico(self):
        return self._medico

    def setMedico(self, medico):
        self._medico = medico

    def getDataCirurgia(self):
        return self._dataCirurgia

    def setDataCirurgia(self, dataCirurgia):
        self._dataCirurgia = dataCirurgia

    def getNomeEspecialidadeMedico(self):
        return self._medico.getNomeEspecialidade()

paciente01 = Paciente("Leandro", "123.456.789-01")
especialidade01 = Especialidade("Cardiologia")
especialidade02 = Especialidade("Ortopedia")
hospital01 = Hospital("Hospital Santa Casa", "987.654.321-98")
medico01 = Medico("Marco", "654.321.598-85", especialidade01, hospital01)
medico02 = Medico("Gabriela", "753.159.852-56", especialidade02, hospital01)
cirurgia01 = Cirurgia("Acromioplastia", paciente01, medico02, "03/12/2020")

paciente01.setMedicoAtende(medico01)
hospital01.setMedicoChefe(medico01)

print("Questão 01 R: {}".format(hospital01.getMedicoChefeEspecialidade()))
print("Questão 02 R: {}".format(medico01.getNomeHospital()))
print("Questão 03 R: {}".format(paciente01.getNomeMedicoAtende()))
print("Questão 04 R: {}".format(paciente01.getCpf()))
print("Questão 05 R: {}".format(hospital01.getCnpj()))
print("Qual a especialidade do médico de uma cirurgia? R: {}".format(cirurgia01.getNomeEspecialidadeMedico()))