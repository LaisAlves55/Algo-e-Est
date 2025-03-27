#ex10.py
# pedir valor da compra ao usuario e usar o comando IF para calcular o desconto de acordo com a faixa de preço 

preco_compra = float(input("Digite o preço da compra: "))

if preco_compra  ==100  <=500:
    
    desconto = preco_compra * 0.1
    print("Desconto de 10%")
elif preco_compra > 500:
    desconto = preco_compra * 0.2
    print("Desconto de 20%")
else :
    desconto = 0
    print("Sem desconto")



