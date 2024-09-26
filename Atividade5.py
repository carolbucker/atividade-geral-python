# Laços

#Solicito ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))
print(f"Tabuado do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    