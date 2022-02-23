#Exercício Relampago Supresa Belos Argo Mento - Leandro Cunha Magalhães e Leonardo Rezende
from modelo.Produto import Produto

produto01 = Produto("Caneta", 200, 1.5, 10, 200)

produto01.debitarEstoque(50)

print(produto01.getQtdeEstoque())