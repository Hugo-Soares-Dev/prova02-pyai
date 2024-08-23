
contato = input('Qual nome gostaria de acrescentar na agenda: ')
numero = input('Informe o Numero: ')
endereco = input('Informe Imail: ')

agenda={'nome': contato, 'telefone': numero, 'email': endereco}

for i in agenda.items():
    print(i)
