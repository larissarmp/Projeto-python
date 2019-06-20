senha = "54321"
leitura = ""
while(leitura != senha):
    leitura = input("Digite a senha:/ type the password: ")
    if leitura == senha:
        input(print ('Acesso liberado'))
    else:
        print ('senha incorreta. Tente novamente')
