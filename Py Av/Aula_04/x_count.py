# Escreva um programa que recebe uma lista de palavras e calcula a média de ocorrências da letra X. 

# Segmente a solução em 3 funções: 

# 1a
# get_user_words() -> List[str]

def get_user_words():
    wList = []

    nWords = int(input("Digite a quantidade de palavras: "))

    for w in range(nWords):
        word = input("Digite uma palavra: ").lower()
        wList.insert(w,word)

    return wList

wList = get_user_words()


# 2a
# count_x_occurrences(word: str) -> int

check = False

def count_x_occurrences(wList: list):
    wCount = len(wList)
    xCount = 0 
    global check

    if check == False:

        for w in range(wCount):

            for l in wList[w]:

                if l == "x":
                    xCount = xCount + 1

        check = True
        return xCount

xCount = count_x_occurrences(wList)

# 3a
# inform_average(average: float) -> None

def inform_average(wList: list, xCount: int):

    average = xCount/len(wList)
    
    return average

average = inform_average(wList,xCount)

print("Você digitou ", len(wList), " palavras, nelas continham ", int(xCount), " letras x." )
print("A média de ocorrências da letra x é: ",average)


