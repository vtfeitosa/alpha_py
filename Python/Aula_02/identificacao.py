#Identificação

S = input("Sexo F/M/I: ")

if S.upper() == "F":
    print("Feminino")

elif S.upper() == "M":
    print("Masculino")

elif S.upper() == "I":
    print("Indefinido")

else:
    print("Inválido")

