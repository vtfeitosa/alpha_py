# Vetores
# Captar duas listas, cada lista em um input, itens separados por espaço

sent1 = input("Digite algo: ").split(" ")
sent2 = input("Digite outro algo: ").split(" ")
lettersList = []

for l in sent2:
  
  for char in sent1:
    if char == l:

      if char not in lettersList:
        lettersList.append(l)

print("O input 1 contem os seguintes caracteres do input 2: ", lettersList)
