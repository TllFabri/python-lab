nome = 'Thiago'
altura = 1.77
peso = 70
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

from datetime import datetime
hoje = datetime.now()
print(f"Hoje é {hoje:%d/%m/%Y}")
