print("Selecione a operação desejada:")
print("1 Para Adição")
print("2 Para Subtração")
print("3 Para Multiplicação")
print("4 Para Divisão")

operacao = input("Digite o número da operação (1/2/3/4): ")


if operacao in ['1', '2', '3', '4']:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if operacao == '1':
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif operacao == '2':
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif operacao == '3':
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    elif operacao == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")