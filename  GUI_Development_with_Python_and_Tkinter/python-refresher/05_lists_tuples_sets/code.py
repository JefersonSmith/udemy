l = ["Bob", "Rolf", "Anne"] #List [] - mantém a ordem dos elementos
t = ("Bob", "Rolf", "Anne") #Tuple () - mantém a ordem dos elementos - não podem ser modificadas
s = {"Bob", "Rolf", "Anne"} #Set {} - não tem elementos duplicados

l[0] = "Smith" #Alterando lista
print(l)

l.append("Rocha") #Adiciona ao final
print(l)

l.remove("Rolf")
print(l)

s.add("Smith") #adiciona elemento ao set
print(s)