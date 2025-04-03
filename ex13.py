#cadastro de alunos de uma escola
nome= input("insira seu nome completo:")
idade= int(input("insira idade:"))
turma= input("insira turma:")
if idade >= 6: 
    print(f"Aluno cadastrado com sucesso: {nome}, {idade} anos, {turma}")
else:
    print("cadastro invalido")
