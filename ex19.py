idade= int(input('insira idade:'))
atleta= str(input('você é atleta?'))
sexo= str(input('qual seu sexo?'))
if idade <15:
    print('artigos infantís')
elif idade >15 and idade<21 and sexo=='feminino':
    print('maquiagem e moda')
elif idade >15 and idade<32 and atleta=='sim' and sexo=='masculino':
    print('artigos esportivos') 
elif idade>15 and idade<21 and atleta=='não' and sexo=='masculino':
    print('videogames')
elif idade >21 and idade<32 and atleta=='não' and sexo=='masculino':
    print ('livros, jardinagem e eletrodomesticos')
elif idade >22 and idade<35 and sexo== 'feminino':
    print('artigos esportivos e itens de casa')
          