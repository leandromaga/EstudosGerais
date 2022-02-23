from modelo.Produto import Produto

produto01 = Produto("Caneta", 200, 1.5, 10, 200)

produto01.creditarEstoque(25)

print(produto01.getQtdeEstoque())
