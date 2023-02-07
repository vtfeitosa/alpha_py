# Captar uma frase e identificar os caracteres e contá-los de acordo com as catergorias:
# Vogal, Consoante, Espaço e Pontuação
# Exibir a porcentagem 

sentence = input("Digite uma frase: ").lower()
v = "aeiou"
c = "bcdfghjklmnpqrstvxyz"

vT = 0
cT = 0
spT = 0
punT = 0

for char in sentence:

  if char == " ":
    spT += 1
  
  elif char in v:
    vT += 1

  elif char in c:
    cT += 1

  else:
    punT += 1

vP = (100*vT)/len(sentence)
cP = (100*cT)/len(sentence)
spP = (100*spT)/len(sentence)
punP = (100*punT)/len(sentence)

print(round(vP,2),"%"," vogais = ",vT)
print(round(cP,2),"%"," consoantes = ",cT)
print(round(spP,2),"%"," espaços = ",spT)
print(round(punP,2),"%"," pontuação = ",punT)
