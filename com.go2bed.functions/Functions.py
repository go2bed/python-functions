def my_fun(string):
    print(string)


my_fun('Hello')


def greeting(name):
    print("Hello " + name)


greeting('Jose')


def add_num(num1, num2):
    return num1 + num2


x = add_num('goo', 'gle')
y = add_num(2, 3)
print(x)
print(y)


def is_prime(num):
    """
    This function checks for prime numbers
    :param num:
    :return:
    """

    for n in range(2, num):
        if num % n == 0:
            print('{} is not a prime'.format(num))
            break

    else:
        print('The {} is prime'.format(num))


is_prime(12)
