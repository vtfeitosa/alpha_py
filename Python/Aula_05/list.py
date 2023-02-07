# Reordenar Lista

nWords = int(input("Digite a quantidade de palavras: "))
wList = []

for w in range(nWords):
  word = input("Digite uma palavra: ")
  wList.insert(w,word)

for i in range(nWords):
  print(wList[(len(wList)-i)-1])