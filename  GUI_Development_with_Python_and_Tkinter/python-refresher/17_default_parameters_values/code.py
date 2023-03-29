def add(x, y=8): # x, y - parameters
    print(x + y)

add(5) #Não precisa informar o y, pois já foi definido como 8

default_y = 3

def add2(x, y=default_y):
    sum = x + y
    print(sum)

add2(2)

default_y = 4 #Uma variável utilizada como parâmetro não pode ser modificada

add2(2)
