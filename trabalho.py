import csv import os

----------------------

Funções utilitárias

----------------------

def carregar_clientes(arquivo): clientes = {} try: with open(arquivo, newline='', encoding='utf-8') as f: leitor = csv.DictReader(f) for linha in leitor: clientes[linha['id']] = { 'nome': linha['nome'], 'banco': linha['banco'], 'saldo': float(linha['saldo']) } except FileNotFoundError: print(f"Arquivo {arquivo} não encontrado.") return clientes

def salvar_clientes(arquivo, clientes): with open(arquivo, 'w', newline='', encoding='utf-8') as f: campos = ['id', 'nome', 'banco', 'saldo'] escritor = csv.DictWriter(f, fieldnames=campos) escritor.writeheader() for cid, dados in clientes.items(): escritor.writerow({ 'id': cid, 'nome': dados['nome'], 'banco': dados['banco'], 'saldo': f"{dados['saldo']:.2f}" })

def carregar_operacoes(arquivo): operacoes = [] try: with open(arquivo, newline='', encoding='utf-8') as f: leitor = csv.DictReader(f) for linha in leitor: operacoes.append(linha) except FileNotFoundError: print(f"Arquivo {arquivo} não encontrado.") return operacoes

----------------------

Operações financeiras

----------------------

def deposito(clientes, cid, valor): if cid in clientes: clientes[cid]['saldo'] += valor return True return False

def saque(clientes, cid, valor): if cid in clientes and clientes[cid]['saldo'] >= valor: clientes[cid]['saldo'] -= valor return True return False

def transferencia(clientes, origem, destino, valor): if origem in clientes and destino in clientes: taxa = 0 if clientes[origem]['banco'] != clientes[destino]['banco']: taxa = valor * 0.05  # 5% total = valor + taxa if clientes[origem]['saldo'] >= total: clientes[origem]['saldo'] -= total clientes[destino]['saldo'] += valor return True return False

----------------------

Funções do menu

----------------------

def mostrar_saldo(clientes, cid): if cid in clientes: print(f"Saldo de {clientes[cid]['nome']}: R$ {clientes[cid]['saldo']:.2f}")

def mostrar_extrato(operacoes, cid): print(f"Extrato de {cid}:") for op in operacoes: if op['id'] == cid or op.get('destino') == cid: print(op)

def executar_operacao(clientes, operacoes): print("1 - Saque") print("2 - Depósito") print("3 - Transferência") opc = input("Escolha: ")

if opc == '1':
    cid = input("ID do cliente: ")
    valor = float(input("Valor: "))
    if saque(clientes, cid, valor):
        operacoes.append({'tipo': 'saque', 'id': cid, 'valor': valor})
        print("Saque realizado.")
    else:
        print("Falha no saque.")

elif opc == '2':
    cid = input("ID do cliente: ")
    valor = float(input("Valor: "))
    if deposito(clientes, cid, valor):
        operacoes.append({'tipo': 'deposito', 'id': cid, 'valor': valor})
        print("Depósito realizado.")
    else:
        print("Falha no depósito.")

elif opc == '3':
    origem = input("ID origem: ")
    destino = input("ID destino: ")
    valor = float(input("Valor: "))
    if transferencia(clientes, origem, destino, valor):
        operacoes.append({'tipo': 'transferencia', 'id': origem, 'destino': destino, 'valor': valor})
        print("Transferência realizada.")
    else:
        print("Falha na transferência.")

----------------------

Execução em lote

----------------------

def executar_lote(arquivo, clientes, operacoes): try: with open(arquivo, 'r', encoding='utf-8') as f: for linha in f: partes = linha.strip().split(',') if partes[0] == 'saque': saque(clientes, partes[1], float(partes[2])) elif partes[0] == 'deposito': deposito(clientes, partes[1], float(partes[2])) elif partes[0] == 'transferencia': transferencia(clientes, partes[1], partes[2], float(partes[3])) except FileNotFoundError: print("Arquivo de lote não encontrado.")

----------------------

Programa principal

----------------------

def main(): clientes = carregar_clientes('cadastro.csv') operacoes = carregar_operacoes('dados.csv')

while True:
    print("\nMenu:")
    print("1 - Saldo")
    print("2 - Extrato")
    print("3 - Operações")
    print("4 - Executar lote")
    print("5 - Sair")
    opc = input("Escolha: ")

    if opc == '1':
        cid = input("ID do cliente: ")
        mostrar_saldo(clientes, cid)

    elif opc == '2':
        cid = input("ID do cliente: ")
        mostrar_extrato(operacoes, cid)

    elif opc == '3':
        executar_operacao(clientes, operacoes)

    elif opc == '4':
        arquivo = input("Nome do arquivo de lote: ")
        executar_lote(arquivo, clientes, operacoes)

    elif opc == '5':
        salvar_clientes('resultado.csv', clientes)
        print("Saindo...")
        break

    else:
        print("Opção inválida.")

if name == "main": main()

