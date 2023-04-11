# Faça um programa em python que faça a divisão de 1 por um valor passado
# por uma variável e realize o tratamento para as entradas abaixo:

# entrada = 0
# divisao = 1/entrada # vai dar error

# #nesse caso tem que ser tratado o erro de divisão por zero, criar um 
# tratamento de exceção para esse tipo de erro e imprimir uma mensagem 
# amigável com o tipo de erro.

# entrada = ‘teste’
# divisao = 1/entrada # vai dar error

# nesse caso tem que ser tratado o erro de tipo, criar um tratamento # exceção
# para esse tipo de erro e imprimir uma mensagem amigável com o tipo de erro.

# E deixar o código para tratar erros genéricos diferentes dos mencionados acima.

# Caso a entrada seja um valor que não provoque erro, imprimir o valor da divisão.

# Por fim, independente de ter erro ou não imprimir ao final da execução do 
# programa, dentro da estrutura de tratamento de exceções uma mensagem 
# informando seu nome.

# Crie esse código, suba para o github e envie na plataforma somente o link do
# repositório com o exercício resolvido.

try:
    inpNum = int(input("Divisor: "))
    quoNum = int(1/inpNum)

except ZeroDivisionError:
    print('O Divisor deve ser maior que zero. Tente novamente com outro número inteiro!')

except ValueError:
    print('O Divisor precisa ser um número inteiro rsrs Tente novamente com um número! :)')

except Exception as error:
    print(f'ERRO: {error}')

else:
    print(f'Quociente da divisão de 1 por {inpNum} é: {quoNum}')

finally:
    print('Vitória')