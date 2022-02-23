# -*- coding: utf-8 -*-
class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

class Aluno(Pessoa):
    def __init__(self, nome):
        Pessoa.__init__(self, nome)


class Professor(Pessoa):
    def __init__(self, nome):
        Pessoa.__init__(self, nome)

class Turma:
    def __init__(self, nome, professor, disciplina):
        self._nome = nome
        self._professor = professor
        self._disciplina = disciplina
        self._alunos = []

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getProfessor(self):
        return self._professor

    def setProfessor(self, professor):
        self._professor = professor

    def getDisciplina(self):
        return self._disciplina

    def setDisciplina(self, disciplina):
        self._disciplina = disciplina

    def getProfessorNome(self):
        return self._professor.getNome()

    def getDisciplinaNome(self):
        return self._disciplina.getNome()

    def alocarAluno(self, aluno):
        self._alunos.append(aluno)

    def listarAlunos(self):
        for aluno in self._alunos:
            print(aluno.getNome())

    def verificarAluno(self, aluno):
        return aluno in self._alunos

    def excluirAluno(self, aluno):
        self._alunos.remove(aluno)

class Curso:
    def __init__(self):
        self._alunos = []
        self._turmas = []

    def alocarAluno(self, aluno):
        self._alunos.append(aluno)

    def listarAlunos(self):
        for aluno in self._alunos:
            print(aluno.getNome())

    def alocarTurma(self, turma):
        self._turmas.append(turma)

    def listarTurmaNome(self):
        for turma in self._turmas:
            print(turma.getNome())

    def listarProfessorTurmas(self):
        for turma in self._turmas:
            print(turma.getProfessorNome())

    def listarAlunosTurma(self):
        for turma in self._turmas:
            turma.listarAlunos()

    def listarDisciplinaTurma(self):
        for turma in self._turmas:
            print(turma.getDisciplinaNome())

    def verificarAluno(self, aluno):
        return aluno in self._alunos

    def verificarTurma(self, turma):
        return turma in self._turmas

    def excluirTurma(self, turma):
        self._turmas.remove(turma)

    def excluirAluno(self, aluno):
        self._alunos.remove(aluno)

class Disciplina:
    def __init__(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

professor01 = Professor("Marco")
professor02 = Professor("Marcos Miguel")
professor03 = Professor("Debora")

disciplina01 = Disciplina("Orientação a Objeto")
disciplina02 = Disciplina("Analise de Sistemas")
disciplina03 = Disciplina("Desing Thinking")

turma01 = Turma("Turma A", professor01, disciplina01)
turma02 = Turma("Turma B", professor02, disciplina02)
turma03 = Turma("Turma C", professor03, disciplina03)

curso01 = Curso()
curso01.alocarTurma(turma01)
curso01.alocarTurma(turma02)
curso01.alocarTurma(turma03)

aluno01 = Aluno("Leandro")
aluno02 = Aluno("Vitória")
aluno03 = Aluno("Carla")
aluno04 = Aluno("Caio")
aluno05 = Aluno("Luna")
aluno06 = Aluno("Gabriel")

curso01.alocarAluno(aluno01)
curso01.alocarAluno(aluno02)
curso01.alocarAluno(aluno03)
curso01.alocarAluno(aluno04)

turma01.alocarAluno(aluno01)
turma01.alocarAluno(aluno02)
turma01.alocarAluno(aluno03)
turma01.alocarAluno(aluno04)
turma02.alocarAluno(aluno05)
turma03.alocarAluno(aluno06)

print("Questão 01:")
print(turma01.getProfessorNome())
print("Questão 02:")
turma01.listarAlunos()
print("Questão 03:")
curso01.listarProfessorTurmas()
print("Questão 04:")
curso01.listarAlunosTurma()
print("Questão 05:")
curso01.listarAlunos()
print("Questão 06:")
curso01.listarDisciplinaTurma()
print("Questão 07:")
print(turma01.verificarAluno(aluno01))
print("Questão 08:")
print(curso01.verificarAluno(aluno05))
print("Questão 09:")
print(curso01.verificarTurma(turma02))
print("Questão 10")
turma01.excluirAluno(aluno02)
turma01.listarAlunos()
print("Questão 11:")
curso01.excluirTurma(turma03)
curso01.listarTurmaNome()
print("Questão 12:")
curso01.excluirAluno(aluno01)
curso01.listarAlunos()