idade = int(input("Digite sua idade:"))
if idade < 18:
    print("Você não tem idade para tirar carteira de motorista")
else: 
    carteira = input("Você tem uma CNH? (s/n):").lower()
if carteira == "s":
    print("Você está apto para dirigir :)")
else: 
    print("Você precisa tirar uma carteira de motorista")