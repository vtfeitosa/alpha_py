inpW = input("Digite uma palavra: ").lower()

finalW = ""

v = "aeiou"

for l in inpW:

  if l not in v:
    finalW += l

print(finalW)

