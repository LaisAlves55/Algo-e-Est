#ex.9
#pedir ao usuariouma temperatura e utilizar o comando IF para determinar se esta frio (<20), morno (>20 e <26), ou quente (>27)


temperatura = float(input("Insira a temperatura: "))

if temperatura <20:
    print("Frio")
elif temperatura >= 20 and temperatura < 26:
    print("Morno")
else:
    print("Quente")
    
