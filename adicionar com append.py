lista = []

adicionar = input("digite os elemnetos que você quer adicionar na lista: ")

while adicionar != "parar":        
        adicionar = input("Adicione elemnetos na lista: ")
        lista.append(adicionar)
      
lista.pop()
print(lista)
