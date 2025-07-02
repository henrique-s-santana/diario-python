import os
os.system('cls')

def somar(a,b): #Função que irá somar
    return a+b

def subtrair(a,b): #Função que irá subtrair
    return a-b

def multiplicar(a,b): #Função que irá multiplicar
    return a*b

def dividir(a,b): #Função que irá dividir
    if b==0:
        return "Erro! Divisão por zero!" #Irá exibir uma mensagem de erro caso o seja feita a tentativa de divisão e algum número por zero
    return a/b

def calculadora_simples():
    print('='*33) #Apenas estética(Opcional)
    print("=======Calculadora Simples=======")
    print('='*33) #Apenas estética(Opcional)
    
    
    #Entrada dos Valores e Operações
    try: #Try e Except = Tratamento de erros para evitar que o programa quebre.
        num1=float(input("Digite um número: "))
        print('-'*33) #Apenas estética(Opcional)
        operacao=str(input("Digite uma operação (+,-,*,/): "))
        print('-'*33) #Apenas estética(Opcional)
        num2=float(input("Digite um número: "))
        print('-'*33) #Apenas estética(Opcional)
        
    except ValueError:
        print("Entrada Inválida!Por favor digite números válidos!")
        return
    
    if operacao == '+':
        resultado = somar (num1,num2)
        
    elif operacao == '-':
        resultado = subtrair (num1,num2)
        
    elif operacao == "*":
        resultado = multiplicar (num1,num2)
        
    elif operacao == '/':
        resultado = dividir (num1,num2)
        
    else:
        resultado = 'Operação Inválida!'
        
    print("Resultado: ", resultado)
    print('='*33) #Apenas estética(Opcional)

#Irá executar a calculadora    
calculadora_simples()    
    
    


