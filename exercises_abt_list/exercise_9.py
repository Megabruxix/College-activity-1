numeros = []

for _ in range(5):
    n = int(input("Digite um número: "))
    numeros.append(n)

maiores = [n for n in numeros if n > 6]

print("Números maiores que 6:", maiores)