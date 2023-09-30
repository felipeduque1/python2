lista_compras = ["leite", "açucar", "arroz", "krokeros"]

print("hoje vou comprar no mercado:", lista_compras)
print(type(lista_compras))
print("a quantidade de elementos na lista é:", len(lista_compras))
#lista_compras.append("pó de café")
lista_compras.remove("leite")
new_lista = sorted(lista_compras)
terceiro_elemento = lista_compras[2]
ultimo_elemento = lista_compras[-1]
lista_compras.pop()

