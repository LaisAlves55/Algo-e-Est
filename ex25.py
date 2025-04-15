#Jogo de Adivinhação com Vetores
# Crie um programa onde o computador sorteia um número entre 1 e 20.
# Armazene os palpites do usuário em uma lista chamada palpites.
# Use um laço while para permitir que o usuário continue tentando até acertar.
# Ao final, exiba todos os palpites que o usuário forneceu.


import random

palpites = []
sorteado = random.randint(1, 20)

while True:
    palpite = int(input("Digite um palpite: "))
    palpites.append(palpite)
    if palpite == sorteado:
        print("Parabéns, vocé acertou o número!")
        break