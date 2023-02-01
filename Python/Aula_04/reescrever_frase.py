# Reescrever frase sem o caractere do input

l = input("Digite os caracteres que deseja remover da frase a seguir: ").lower()
sent = input("Digite uma frase: ").lower()
finalSentence = ""

for c in sent:
  if c != l:
    finalSentence = finalSentence + c

print("Frase Original:",sent)
print("Caractere Removido: ",l)
print("Frase Final: ",finalSentence)