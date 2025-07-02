import os 
os.system('cls')

#Irá definir o acesso do ADM
user_adm = 'Admin123'
password_adm = '12345'

#Irá definir o acesso de um usuário padrão
user_padrao = 'User123'
password_padrao = '12345'

#Irá definir o acesso de um usuário padrão
user_padrao1 = 'User444'
password_padrao1 = '12345'

#Irá definir o acesso de um usuário padrão
user_padrao2 = 'User333'
password_padrao2 = '12345'

#Área de inserção de dados do usuário
user = input('Digite seu usuário: ')
password = input('Digite sua senha: ') 

#Irá verificar se o usuário e senha são do ADM
if user == user_adm and password == password_adm:
    print('Login ADM bem sucedido!')
 
 #Irá verificar se o usuário e senha são do Usuário Padrão   
elif user == user_padrao and password == password_padrao:
    print('Login bem sucedido!')
    
elif user == user_padrao1 and password == password_padrao1:
    print('Login bem sucedido 1!')
    
elif user == user_padrao2 and password == password_padrao2:
    print('Login bem sucedido 2!')    

#Irá apresentar um erro caso o Usuário e Senha estejam errados    
else:
    print('Usuário ou Senha Incorretos!')