# Write a function that computes the volume of a sphere given its radius.
import math

volume = lambda rad: 4 / 3 * math.pi * rad ** 3
print('THe volume of sphere with given radius is :', volume(7))


# Write a function that checks whether a number is in a given range (Inclusive of high and low)

def ran_check(num, low, high):
    if low < num < high:
        print('The {} is  in range between {} and {} '.format(num, low, high))
    else:
        print('The {} is not in range between {} and {} '.format(num, low, high))


def ran_bool(num, low, high):
    return low < num < high


print(ran_check(3, 1, 10))
print(ran_bool(3, 1, 10))

# Write a Python function that accepts a string and calculate
# the number of upper case letters and lower case letters.

sample = 'Hello Mr. Rogers, how are you this fine Tuesday?'


def up_low(sample):
    low_counter = 0
    up_counter = 0
    for letter in sample:
        if letter.islower():
            low_counter += 1
        if letter.isupper():
            up_counter += 1
    print('of Upper case characters :', up_counter)
    print('of Lower case Characters :', low_counter)


up_low(sample)

# Write a Python function that takes a list and returns
# a new list with unique elements of the first list.

l = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]


def unique_list(l):
    a = set()
    for value in l:
        a.add(value)
    return list(set(a))


print(unique_list(l))

# Write a Python function to multiply all the numbers in a list.

numbers = [1, 2, 3, -4]
global product


def multiply(numbers):
    product = 1
    for value in numbers:
        product *= value
    return product


print(multiply(numbers))


# Write a Python function that checks whether a passed string is palindrome or not.

def is_palindrome(s):
    return s[::-1] == s


print(is_palindrome('lol'))

# Write a Python function to check whether a string is pangram or not.

import string

s = "The quick brown fox jumps over the lazy dog"

def is_pangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(is_palindrome(s))