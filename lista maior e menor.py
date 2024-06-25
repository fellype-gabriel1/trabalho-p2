lista = []
contador = 0
n_lista = int(input("digite quantos numeros tem sua lista: "))

while contador < n_lista:
    add_lista = int(input("digite os numeros da sua lista: "))
    lista.append(add_lista)
    contador = contador + 1

print("o maior número da sua lista é:",max(lista))
print("o menor número da sua lista é:",min(lista))