from modelo.Produto import Produto
from modelo.Venda import Venda
from modelo.Cliente import Cliente

produto01 = Produto("Caneta", 100, 1.5, 10, 200)
cliente01 = Cliente("Marco", "753")
venda01 = Venda("15/01", cliente01, produto01, 95)

produto01.vender("25/10", cliente01,30)
produto01.exibirHistorico()