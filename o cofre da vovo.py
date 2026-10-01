while True:
    senha = input("Digite sua senha:  ")

    if len(senha) != 4:
        print("A senha precisa ter exatamente 4 dígitos!")
        continue

    if senha == "1234":
        print("Bem-vinda de volta, vovó!")
        break
    else:
        print("SENHA INCORRETA")