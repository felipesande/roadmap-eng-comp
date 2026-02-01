# Calculadora simples
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print(num1, "+", num2, "=", soma)
print(num1, "-", num2, "=", sub)
print(num1, "*", num2, "=", mult)
print(num1, "/", num2, "=", div)

# Conversor de temperatura
c = float(input("Digite a temperatura em graus Celsius: "))

f = (9/5 * c) + 32
k = c + 273.15

print("A temperatura em graus Fahrenheit é", f, "°F")
print("A temperatura em Kelvin é", k, "K")

# Programa que recebe nome e idade
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Olá, meu nome é " + nome + " e eu tenho " + str(idade) + " anos!")
