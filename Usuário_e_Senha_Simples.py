import os
os.system('cls')


user_correct = 'admin' #Define o nome do usuário.
password_correct = '12345' #Define a senha do usuário.

#Área onde o usuário irá digitar suas informações.
user = input("Digite seu usuário: ")
password = input("Digite sua senha: ")

#Irá verificar se Usuário e Senha digitados pelo usuário são os mesmos cadastrados.
if user == user_correct and password == password_correct: 
    print('Login bem sucedido!')

#Se o Usuário ou Senha estiver incorretos irá voltar está mensagem ao Usuário.  
else:
    print('Usuário ou Senha Incorretos!')
        
    
    

