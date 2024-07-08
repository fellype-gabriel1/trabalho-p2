numero = int(input("Digite um número: "))

if numero <= 1:
    n_perfeito = False
else:

    soma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i
    

    n_perfeito = (soma_divisores == numero)

if n_perfeito:
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")