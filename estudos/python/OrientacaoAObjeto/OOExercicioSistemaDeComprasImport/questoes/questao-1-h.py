from modelo.Produto import Produto
from modelo.Compra import Compra
from modelo.Fornecedor import Fornecedor

produto01 = Produto("Caneta", 100, 1.5, 10, 200)
fornecedor01 = Fornecedor("Leandro", 321)
compra01 = Compra("25/11", produto01, fornecedor01, 50, 1.50)

produto01.comprar("25/10", fornecedor01, 50, 1.5)
produto01.exibirHistorico()