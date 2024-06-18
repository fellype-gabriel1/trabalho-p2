fila_banco = []

espera = int(input("quantos clientes estão na fila de espera? "))
contador = 0

while contador < espera:
    cliente_espera = str(input("me fale o nome dos clintes: "))
    fila_banco.append(cliente_espera)
    contador = contador + 1   

while fila_banco:
    cliente = fila_banco.pop(0)
    print(f"cliente {cliente} está sendo atendido(a)")
    print(fila_banco)