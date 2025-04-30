num1 = []
for i in range (4):
    num2= float(input("Digite um número:"))
    num1.append(num2)
for i in num1: 
    if i % 2 == 0:
        print(i)