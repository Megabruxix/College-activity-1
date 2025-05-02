nmr1 = float(input("Digite um número:"))
nmr2 = float(input("Digite outro número:"))
def soma (): 
    return nmr1 + nmr2 

soma_float = float(soma ())
soma_int = int(soma ())
if soma_float == soma_int:
    print("A soma int é igual a soma float dos seus números")
else:
    print("A soma int não é igual a soma float dos seus números")