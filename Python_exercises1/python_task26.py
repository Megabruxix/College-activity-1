numero = input("Digite um número qualquer: ")
casas = len(numero.split('.')[-1]) if '.' in numero else 0
print("Casas decimais:", casas)