senha = "12345"
senha_usuario = input("Diga sua senha: ")
tentativas = 1
while senha != senha_usuario and tentativas <= 3: 
    print("errou haha")
    senha_usuario = input("Diga sua senha: ")
    tentativas += 1
if senha == senha_usuario:
    print("Acertou")
else:
    print("Limite de tentativas atingido")