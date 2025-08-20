# if / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Parabéns você entrou!')
    print('Bem vindo ao sistema!')

elif entrada == 'sair':
    print('Você saiu!')

else:
    print('Dado invalido!')


print('FORA DOS IFS')