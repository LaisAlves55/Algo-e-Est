#ex8.py
# pedir ao usuario um nome de usuario e senha e usar comando IF para verificar se as credenciais estao corretas

nome_usuario = input("Digite seu nome de usuario: ")

senha = input("Digite sua senha: ")

if nome_usuario == "admin" and senha == "123456":
    print("Login efetuado com sucesso!")
    print("Acesso permitido!")

else:
    print("Login ou senha incorretos!")
    print("Acesso negado!")
    print("Tente novamente!")
    
    


