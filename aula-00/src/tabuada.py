"""Passo 2 da atividade: ler um número e imprimir a sua tabuada."""

numero = int(input("Digite um número inteiro: "))

print(f"\nTabuada do {numero}:")
for multiplicador in range(1, 11):
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
