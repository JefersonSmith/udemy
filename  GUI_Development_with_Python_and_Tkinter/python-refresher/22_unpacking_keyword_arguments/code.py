def named(**kwargs):
    print(kwargs)


named(name="bob", age=25)

def named2(name, age):
    print(name, age)


print("=-="*5)

details = {"name": "Bob", "age": 25}

named2(**details)

print("=-="*5)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f'{arg}: {value}')

print_nicely(name="Bob", age=25)

print("=-="*5)

def both(*args, **kwargs):
    print(args)
    print((kwargs))

both(1, 3, 5, name="Bob", age=25)
