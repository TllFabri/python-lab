def calculadora():
    print("Calculadora Simples")
    print("Operações disponíveis: +, -, *, /")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        op = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        
        if op == '+':
            resultado = num1 + num2
        elif op == '-':
            resultado = num1 - num2
        elif op == '*':
            resultado = num1 * num2
        elif op == '/':
            if num2 == 0:
                return "Erro: Divisão por zero!"
            resultado = num1 / num2
        else:
            return "Operação inválida!"
            
        return f"Resultado: {num1} {op} {num2} = {resultado}"
        
    except ValueError:
        return "Erro: Entrada inválida! Use números válidos."

print(calculadora())