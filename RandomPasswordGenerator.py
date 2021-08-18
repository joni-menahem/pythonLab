import string
import random


def RandomPasswordGenerator(length):
    password = ""
    for i in range(length):
        lower = random.choice(string.ascii_lowercase)
        upper = random.choice(string.ascii_uppercase)
        sign = random.choice("!@#$%^&*")
        number = random.choice(string.digits)
        data = [lower, upper, sign, number]
        possible = random.choice(data)
        password = password + possible
    return password


x = 64
pwd = RandomPasswordGenerator(x)
print(pwd)
