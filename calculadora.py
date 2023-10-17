def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

while True:
    print("1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair")
    opcao = input("Escolha a operação desejada: ")

    if opcao == "0":
        print("Saindo da calculadora.")
        break

    if opcao in ["1", "2", "3", "4"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = soma(num1, num2)
        elif opcao == "2":
            resultado = subtracao(num1, num2)
        elif opcao == "3":
            resultado = multiplicacao(num1, num2)
        elif opcao == "4":
            resultado = divisao(num1, num2)

        print(f"Resultado: {resultado}")
    else:
        print("Essa opção não existe. Tente novamente.")
