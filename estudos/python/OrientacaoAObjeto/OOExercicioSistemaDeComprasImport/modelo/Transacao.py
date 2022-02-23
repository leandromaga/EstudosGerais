class Transacao:
    def __init__(self, dataTransacao, produto, qtde):
        self._dataTransacao = dataTransacao
        self._produto = produto
        self._qtde = qtde

    def getDataTransacao(self):
        return self._dataTransacao

    def setDataTransacao(self, dataTransacao):
        self._dataTransacao = dataTransacao

    def getProduto(self):
        return self._produto

    def setProduto(self, produto):
        self._produto = produto

    def getQtde(self):
        return self._qtde

    def setQtde(self, qtde):
        self._qtde = qtde