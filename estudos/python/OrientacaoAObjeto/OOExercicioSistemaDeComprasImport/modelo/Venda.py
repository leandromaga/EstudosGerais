from .Transacao import Transacao

class Venda(Transacao):
    def __init__(self, dataTransacao, cliente, produto, qtde):
        Transacao.__init__(self, dataTransacao, produto, qtde)
        self._cliente = cliente

    def vender(self, produto, qtdeVendida):
        if (produto == self._produto and produto.verificarEstoqueInsuficiente(qtdeVendida)) == True:
            print("Quantidade do estoque insuficiente!")
            return False
        else:
            produto.debitarEstoque(qtdeVendida)
            print("Valor da venda R$ {}".format(qtdeVendida * produto.getPrecoUnit()))
            produto.verificarEstoqueBaixo()
            return True