def square(num):
    result = num ** 2
    return result


print(square(2))


def square(num):
    return num ** 2


print(square(4))


def square(num): return num ** 2


print(square(3))

lambda num: num ** 2
print(lambda num: num ** 2)

square = lambda num: num ** 2

print(square(10))

# Check if a number is even

even = lambda num: num % 2 == 0
print(even(4))


def even(num):  # the same as lambda
    return num % 2 == 0


print(even(4))

# Grabs the first character of the string

first = lambda s: s[0]
print(first('hello'))

rev = lambda s: s[::-1]
print(rev('hello'))


#########

def adder(x, y):
    return x + y


print(adder(10, 12))

adder = lambda x, y: x + y

print(adder(30, 30))

len_check = lambda item: len(item)

print(len_check('how many chars this string have'))


