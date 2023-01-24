#Hipermercado Tabajara - Promoção de Carnes

print("Opções de Carne:")
print("1 - Filé Duplo")
print("2 - Alcatra")
print("3 - Picanha")

numCarne = int(input("Qual o número correspondente a opção de carne? "))
peso = int(input("Qual a quantidade de carne em Kg? "))

if numCarne == 1:

  if peso <= 5:
    total = peso * 5.8
  
  else:
    total = peso * 4.9

  print(peso, "kg de Filé Duplo, total de R$", total)
  
elif numCarne == 2:

  if peso <= 5:
    total = peso * 6.8
  else:
    total = peso * 5.9

  print(peso, "kg de Alcatra, total de R$", total)

elif numCarne == 3:
  
  if peso <= 5:
    total = peso * 7.8
  else:
    total = peso * 6.9

  print(peso, "kg de Picanha, total de R$", total)

print("Opções de Pagamento:")
print("1 - Cartão")
print("2 - Á Vista")

opcPag = int(input("Qual o número correspondente a opção de pagamento? "))

if opcPag == 1:
  desc = (5 * total)/100
  total = total - desc

  print("O valor total para pagamento no cartão é: R$", total)
  print(" O desconto do cartão foi de: R$ ", desc)
  
else:
  print("O valor total para pagamento á vista é: R$", total)

