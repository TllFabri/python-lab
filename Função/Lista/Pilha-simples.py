def inverter_lista(lista):
    return lista[::-1]

pilha = []

print("Digite comandos (PUSH x, POP ou SAIR para encerrar):")
while True:
    comando = input("> ").strip()

    if comando.upper() == "SAIR":
        break
    elif comando.upper().startswith("PUSH "):
        try:
            valor = comando.split()[1]
            pilha.append(valor)
        except IndexError:
            print("Uso correto: PUSH <valor>")
    elif comando.upper() == "POP":
        if pilha:
            removido = pilha.pop()
            print(f"Removido: {removido}")
        else:
            print("A pilha está vazia!")
    else:
        print("Comando inválido! Use PUSH x, POP ou SAIR.")

print("\nPilha final (topo → base):")
if pilha:
    topo_base = inverter_lista(pilha)
    print(topo_base)
else:
    print("Pilha vazia.")
