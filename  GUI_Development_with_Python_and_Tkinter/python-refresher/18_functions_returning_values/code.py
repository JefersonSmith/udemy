def add(x, y):
    print(x + y)

add(5, 8)
result = add(5, 8)
print(result) #none

print("=-="*5)

def add1(x, y):
    return x + y

add(5, 8)
result = add1(5, 8)
print(result)

print("=-="*5)

def add2(x, y):
    return x + y
    print(x + y)
result = add2(5,8)
print(result)

print("=-="*5)

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

result = divide(15, 0)
print(result)