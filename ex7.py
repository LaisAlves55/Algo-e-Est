# receber dois numeros e uma operaçao (adiçao , subtraçao, multiplicaçao e divisao). Utilizar If para realizar a operaçao correta com base na escolha do usuario.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
   adicao= numero1+numero2
   print("Resultado da soma: ", adicao)
elif operacao == "-":
    subtracao = numero1 - numero2
    print("Resultado da subtração: ", subtracao)  

elif operacao == "*":
    multiplicacao = numero1 * numero2
    print("Resultado da multiplicação: ", multiplicacao)
elif operacao =="/":
    divisao= numero1 / numero2
    print("Resultado da divisão: ", divisao)
else:
    print("Operação inválida!")




