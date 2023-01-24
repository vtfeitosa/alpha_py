#Maior e Menor

a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
c = int(input("Valor 3: "))

maiorAB = (a + b + abs(a - b))/2
maiorABC =(maiorAB + c + abs(maiorAB - c))/2

print("Maior Valor é: " , maiorABC)
