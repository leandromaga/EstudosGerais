from modelo.Produto import Produto

produto01 = Produto("Caneta", 100, 1.5, 10, 200)

print(produto01.verificarEstoqueExcedente(300))