idade=int(input('insira idade:'))
if idade >=18:
    print('liberado')
else:
    print('idade insuficiente')
membro= str(input('você é membro?'))
if membro=='não':
    print('o valor do ingresso é 500')
else:
    print('liberado')
a_membro= str(input('você esta acopanhado de um menbro?'))
if a_membro=='sim':
    print('a meia entrada é 250')


