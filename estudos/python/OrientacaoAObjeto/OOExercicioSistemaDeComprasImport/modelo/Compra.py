from .Transacao import Transacao

class Compra(Transacao):
    def __init__(self, dataTransacao, produto, fornecedor, qtde, precoUnit):
        Transacao.__init__(self, dataTransacao, produto, qtde)
        self._precoUnit = precoUnit
        self._fornecedor = fornecedor

    def comprar(self, produto, qtdeCompra):
        if (produto == self._produto and produto.verificarEstoqueExcedente(qtdeCompra)) == True:
            print("Estoque com limite exedente!")
            return False
        else:
            produto.creditarEstoque(qtdeCompra)
            return True