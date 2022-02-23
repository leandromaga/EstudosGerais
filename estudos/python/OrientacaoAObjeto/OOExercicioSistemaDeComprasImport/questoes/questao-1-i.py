from modelo.Produto import Produto
from modelo.Compra import Compra
from modelo.Fornecedor import Fornecedor

produto01 = Produto("Caneta", 100, 1.5, 10, 200)
fornecedor01 = Fornecedor("Leandro", 321)
compra01 = Compra("25/05", produto01, fornecedor01, 50, 1.50)

compra01.comprar(produto01, 50)

produto01.registrarHistorico(compra01)