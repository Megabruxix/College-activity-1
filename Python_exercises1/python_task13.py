num1 = int(input("Digite um número:"))
if num1 < 18:
    print("Você é menor de idade")
elif num1 >= 18 and num1 <= 60:
    print("Você é maior de idade")
else: 
    print("Você é idoso")