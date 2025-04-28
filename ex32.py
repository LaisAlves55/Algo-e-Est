tabuada_personalizada= int(input("insira base:")) 
int(input("insira inicio:")) 
int(input("insira fim:"))
def tabuada_personalizada(base, inicio, fim):
    print(f"tabuada do{base} de {inicio} até {fim}:")
    for j in range (inicio, fim +1):
        print(f"{base} X {j} = {base *j}")
        
        
tabuada_personalizada= (base, inicio, fim)