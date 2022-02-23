from .Venda import Venda
from .Compra import Compra

class Produto:
    def __init__(self, nome, qtdeEstoque, precoUnit, estoqueMinimo, estoqueMaximo):
        self._nome = nome
        self._qtdeEstoque = qtdeEstoque
        self._precoUnit = precoUnit
        self._estoqueMinimo = estoqueMinimo
        self._estoqueMaximo = estoqueMaximo
        self._historico = []

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getQtdeEstoque(self):
        return self._qtdeEstoque

    def setQtdeEstoque(self, qtdeEstoque):
        self._qtdeEstoque = qtdeEstoque

    def getPrecoUnit(self):
        return self._precoUnit

    def setPrecoUnit(self, precoUnit):
        self._precoUnit = precoUnit

    def getEstoqueMinimo(self):
        return self._estoqueMinimo

    def setEstoqueMinimo(self, estoqueMinimo):
        self._estoqueMinimo = estoqueMinimo

    def getEstoqueMaximo(self):
        return self._estoqueMaximo

    def setEstoqueMaximo(self, estoqueMaximo):
        self._estoqueMaximo = estoqueMaximo

    def debitarEstoque(self, quantidade):
        self.setQtdeEstoque(self.getQtdeEstoque() - quantidade)

    def creditarEstoque(self, quantidade):
        self.setQtdeEstoque(self.getQtdeEstoque() + quantidade)

    def verificarEstoqueBaixo(self):
        return self._qtdeEstoque < self._estoqueMinimo

    def verificarEstoqueInsuficiente(self, quantidade):
        return quantidade > self._qtdeEstoque

    def verificarEstoqueExcedente(self, quantidade):
        return quantidade + self._qtdeEstoque > self._estoqueMaximo

    def calcularValorVenda(self, quantidade):
        return quantidade * self._precoUnit

    def registrarHistorico(self, transacao):
        self._historico.append(transacao)

    def exibirHistorico(self):
        for transacao in self._historico:
            print(transacao)

    def vender(self, dataVenda, cliente, qtdeVendida):
        venda = Venda(dataVenda, cliente, self,qtdeVendida)
        if (venda.vender(self, qtdeVendida)) == True:
            self.registrarHistorico("Venda. Data: {} | Produto: {} | Quantidade: {} | Cliente: {}".format(dataVenda, self.getNome(), qtdeVendida, cliente.getNome()))
            print("Produto registrado com Sucesso.")

    def comprar(self, dataCompra, fornecedor, qtdeCompra, preçoUnit):
        compra = Compra(dataCompra, self, fornecedor, qtdeCompra, preçoUnit)
        if (compra.comprar(self, qtdeCompra) == True):
            self.registrarHistorico("Compra. Data: {} | Produto: {} | Quantidade: {} | Preço Unitário: R$ {} | Fornecedor: {}".format(dataCompra, self.getNome(), qtdeCompra, preçoUnit, fornecedor.getNome()))
            print("Produto registrado com Sucesso.")
