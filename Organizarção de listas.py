comidas = ['leite', 'couve','computador', 'tomate','garfo','faca','tablet','refrigerante']
bebidas = ['uva', 'colher','TV','vinho','cerveja','celular','banana']
talheres = ['arroz','iPhone', 'concha','whisky','vodka','feijão','colher de chá']
eletronicos = []

comidas.remove("computador")
comidas.remove("tablet")
comidas.remove("garfo")
comidas.remove("faca")
comidas.remove("refrigerante")
comidas.remove("leite")

comidas.append("uva")
comidas.append("banana")
comidas.append("arroz")
comidas.append("feijão")

bebidas.remove("colher")
bebidas.remove("TV")
bebidas.remove("celular")
bebidas.remove("uva")
bebidas.remove("banana")

bebidas.append("leite")
bebidas.append("refrigerante")
bebidas.append("whisky")
bebidas.append("vodka")

talheres.remove("arroz")
talheres.remove("iPhone")
talheres.remove("whisky")
talheres.remove("vodka")
talheres.remove("feijão")

talheres.append("garfo")
talheres.append("faca")
talheres.append("colher")


eletronicos.append("iphone")
eletronicos.append("tablet")
eletronicos.append("TV")
eletronicos.append("computador")
eletronicos.append("celular")


print("comidas ->", comidas)
print("bebidas ->", bebidas)
print("talheres ->" ,talheres)
print("eletronicos ->", eletronicos)





