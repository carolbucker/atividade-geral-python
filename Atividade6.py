# Exceções e laços

## Solicita ao usuário um número inteiro

try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou um número: {numero}")
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")
    