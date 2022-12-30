# Nessa aula, vamos aprender como criar estruturas condicionais aninhadas,
# usando os comandos if.. elif.. else em programas Python.

nome = str(input('Qual é o seu nome? '))

if nome.upper() == 'DAVI':
    print('Que nome bonito!')
elif nome.upper() == 'PEDRO' or nome.upper() == 'MARIA' or nome.upper() == 'PAULO':
    print('Seu nome é bem popular no Brasil.')
elif nome.upper() in 'ANA CLÁUDIA JÉSSICA JULIANA':
    print('Belo nome feminino.')
elif nome.upper() in 'ANA CLODISVALDA MARIA FATIMA':
    print('Que belo nome feminino')
else:
    print('Seu nome é tão normal!')
print('Prazer em te conhecer {}!'.format(nome.capitalize()))

