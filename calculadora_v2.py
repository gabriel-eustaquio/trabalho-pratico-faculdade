def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao == 'adicao':
        return adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
        return subtracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao':
        return multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
        return divisao(num1, num2)
    return "Operação inválida"

saida = ''

while saida.lower() != 'n':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    resultado = calculadora(num1, num2, operacao)

    print(f"Resultado da operação: {resultado}")

    saida = input("Deseja continuar (S/N)? ")

print("Programa encerrado.")
