def add(x, y):
    return x + y

print(add(5, 7))

print("=-=" * 5)

add = lambda x,y: x + y

print(add(5, 7))

print("=-=" * 5)

print((lambda x, y: x + y)(5, 7))

print("=-=" * 5)

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]

doubled = list(map(double, sequence))
# doubled = [double(x) for x in sequence]
# doubled = [x * 2 for x in sequence]

print(doubled)

print("=-=" * 5)

sequence2 = [1, 3, 5, 9]
doubled2 = [(lambda x: x * 2)(x) for x in sequence2]
doubled2 = list(map(lambda x: x * 2, sequence2))

