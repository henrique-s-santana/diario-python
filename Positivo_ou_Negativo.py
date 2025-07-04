import os
os.system('cls')

#Solicita que o usuário digite um número
numero = int(input('Digite um número e irei dizer se é positivo ou negativo: '))

#Irá verificar se o número digitado é menor que zero
if numero <0:
    print('Esse número é negativo!')

#Irá verificar se o número digitado é igual a zero    
elif numero == 0:
    print('Esse é um número neutro!')
 
#Se o número digitado não for zero ou menor que zero será positivo  
else:
    print('Esse número é positivo!')