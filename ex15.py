#simulação de compra no mercado
nome_produto, quantidade, preço= input("insira nome do produto:"), int(input("quantidade:")), float(input("Preço unitario:"))
valor_final= preço * quantidade 
if valor_final >= 100:
    print(f"você ganhou 5% de desconto! valor final:{valor_final- valor_final*0.05}")
else:
    print(f"valor final = {valor_final}")