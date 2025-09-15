def myFunc1(*args): #packing
    for i in args:
        print(i)

myFunc1(1, 2, 3)
print()
def myFunc2(args):
    for i in args:
        print(i)

myFunc2([1, 2, 3])
print()

a, b, c = [1, 2, 3] #unpacking
print(f'a: {a}, b: {b}, c: {c}')