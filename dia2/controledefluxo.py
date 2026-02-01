# if, elif e else
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

# for (repetição com limite), range(início, fim, passo)
for i in range(5):
    print(i)
for i in range(1, 5):
    print(i)
for i in range(1, 5, 2):
    print(i)
# ele começa de 0 se não tiver início e vai até fim - 1

# while (repetição com condição)
senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")

print("Acesso liberado")
# string vazia é ""
# Uma variável "vazia" no sentido geral é None

# break (encerra o loop)
for x in range(10):
    if x == 5:
        break
    print(x)

# continue (pula para a próxima repetição)
for y in range(5):
    if y == 2:
        continue
    print(y)
