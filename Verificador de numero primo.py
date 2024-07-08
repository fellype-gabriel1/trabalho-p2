n1 = int(input('digite um número para descobrir se é primo ou não: '))
num_primo = 0

for n in range(1, (n1 + 1)):        
  if n1 % n == 0:
    num_primo += 1
    
if num_primo  == 2 :
  print('é primo')
else:
  print('não é primo') 