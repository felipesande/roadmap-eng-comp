# Verificador de número primo
num = int(input("Digite um número inteiro: "))
# um número primo é um número natural maior que 1 que possui
# apenas 2 divisores positivos e distintos:
# o número 1 e ele mesmo
# número natural (números inteiros não negativos)
if num <= 1:
    print("Não é primo")
elif num == 2:
    print("É primo")
else:
    for i in range(2, num):
        resto = num % i
        if resto == 0:
            print("Não é primo")
            break
        elif i == (num - 1):
            print("É primo")

# Jogo de adivinhação
secreto = 73
print("Tente adivinhar qual é o número secreto!")
print("Dica: O número secreto está entre 0 e 100")
x = None
tentativas = 1
while x != secreto:
    print("tentativa número", tentativas)
    x = int(input("Digite um número: "))
    if x < secreto:
        print("Seu chute foi menor que o número secreto")
        print("Tente novamente")
    elif x > secreto:
        print("Seu chute foi maior que o número secreto")
        print("Tente novamente")
    tentativas = tentativas + 1
print("Você acertou em", (tentativas - 1), "tentativa(s)")
print("Correto, você achou o número secreto, Parabéns!")

# Menu interativo no terminal
while True:
    print("-------------- MENU --------------")
    print("1 - Somar dois números")
    print("2 - Verificar se um número é primo")
    print("3 - Sair")
    print("----------------------------------")
    escolha = int(input("Escolha o que deseja fazer: "))
    print("----------------------------------")
    if escolha == 1:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 + num2
        print(num1, "+", num2, "=", soma)
    elif escolha == 2:
        print("Vamos verificar se o número é primo")
        num = int(input("Digite um número inteiro: "))
        if num <= 1:
            print("Não é primo")
        elif num == 2:
            print("É primo")
        else:
            for i in range(2, num):
                resto = num % i
                if resto == 0:
                    print("Não é primo")
                    break
                elif i == (num - 1):
                    print("É primo")
    elif escolha == 3:
        break
    else:
        print("Você digitou um número inválido")
