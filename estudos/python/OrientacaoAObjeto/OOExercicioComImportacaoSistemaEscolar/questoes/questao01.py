from modelo.Professor import Professor
from modelo.Disciplina import Disciplina
from modelo.Turma import Turma

professor01 = Professor("Marco")
disciplina01 = Disciplina("Orientação a Objeto")
turma01 = Turma("Turma A", professor01, disciplina01)

print("Questão 01:")
print(turma01.getProfessorNome())