lista_aula = []
for presenca in range(1,31):
    nomes = str(input("digite o nome do aluno: "))
    lista_aula.append(nomes)
    if nomes == "fim":
        lista_aula.remove('fim')
        print(lista_aula)
        break