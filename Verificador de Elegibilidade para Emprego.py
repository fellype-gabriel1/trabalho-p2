#Verificador de Elegibilidade para Emprego
idade = int(input("Me informe sua idade "))
nacionalidade = str(input("me  informe sua nacionalidade "))
anos_de_exp = int(input("você tem quantos anos de experiência? "))

if idade >= 18 and anos_de_exp >= 2:
    if nacionalidade == "brasileira" or "brasileiro" :
         print("você está elegivel ao cargo")
else:
    print("você está inelegivel ao cargo")
