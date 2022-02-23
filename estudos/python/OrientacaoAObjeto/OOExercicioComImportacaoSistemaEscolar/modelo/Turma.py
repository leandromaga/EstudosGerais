from .Professor import Professor
from .Disciplina import Disciplina

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