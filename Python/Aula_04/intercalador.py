# Concatenar duas strings, intercalando letra por letra

wordsInp = input("Digite duas palavras separadas por espaço: ").split(" ")
finalStr = ""

if len(wordsInp[0]) > len(wordsInp[1]):
  smWord = wordsInp[1]
  lgWord = wordsInp[0]

else:
  smWord = wordsInp[0]
  lgWord = wordsInp[1]

round = (len(smWord)+ len(lgWord))

for i in range(len(smWord)):  
  finalStr += lgWord[i]
  finalStr += smWord[i]
  leftLetters = i

if len(finalStr) < round:

  for i in range(round-len(finalStr)):
    finalStr += lgWord[leftLetters+i+1]

print(finalStr)