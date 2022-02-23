from modelo.Produto import Produto
from modelo.Venda import Venda
from modelo.Cliente import Cliente

produto01 = Produto("Caneta", 100, 1.5, 10, 200)
cliente01 = Cliente("Leandro", 123)
venda01 = Venda("25/10", cliente01, produto01, 50)

produto01.vender("25/10", cliente01, 50)
produto01.exibirHistorico()