# Verificar se na frase contém todas as letras do alfabeto.
# Se sim, é Pangrama.
# O programa deve mostrar o resultado SIM ou NÃO

sentence = input("Digite uma frase: ").lower()
alphabet = "abcdefghijklmnopqrstuvxyz"
result = ""

for l in alphabet:

  if l in sentence:
    result = "True"
    print(l, "está ")

  else:
    print(l, "não está")
    result = "False"
    break

if result == "True":
  print("SIM, é pangrama. Todas as letras do alfabeto estão na frase :)")

else:
  print("NÃO é pangrama. Nem todas as letras do alfabeto estão na frase :/ ")
