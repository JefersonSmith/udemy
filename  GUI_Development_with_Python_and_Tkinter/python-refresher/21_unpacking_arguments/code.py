def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total

print(multiply(1, 3, 5))

print("=-="*5)

def add(x , y):
    return x + y

nums = [3, 5]
print(add(*nums))
print(add(x=3, y=5))

nums2 = {"x": 15, "y": 25}
print(add(nums2["x"], nums2["y"]))
print(add(x=nums2["x"], y=nums2["y"]))
print(add(**nums2))
# os 3 prints acima são iguais

def multiply2(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

def apply(*args, operator):
    if operator == "*":
        return multiply2(*args)
    elif operator == "+":
        return sum((args))
    else:
        return "No valid operator provided to apply()."

print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 6, 7, operator="*"))