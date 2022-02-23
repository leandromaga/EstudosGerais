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