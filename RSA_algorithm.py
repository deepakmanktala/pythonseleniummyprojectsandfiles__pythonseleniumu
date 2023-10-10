# import GCD from math
from random import randint, randrange
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

while True:
    num = random_with_N_digits(10000)

    if num > 1:
    # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                # break
            else:
                print(num,"is a prime number to be used for RSA")
                break
            # if input number is less than
            # or equal to 1, it is not prime
        else:
            print(num,"is not a prime number")
        break