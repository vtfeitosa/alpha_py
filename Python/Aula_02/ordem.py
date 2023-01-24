#Ordem Crescente e Decrescente

N1 = int(input("Número 1: "))
N2 = int(input("Número 2: "))
N3 = int(input("Número 3: "))

lista = [N1,N2,N3]

print("Ordem de Digitação: [", N1, N2, N3, "]")
print("Ordem Crescente: ", sorted(lista))
print("Ordem Decrescente: ", sorted(lista, reverse = True))
