
from parcial2obj import Alcholicas, Virgenes, Cliente
from parcial2utils import num_verify, verify_str, yes_no, simple_numverify, fibonacci


def fibonacci (num_tofind, num0, num1):
    limit = 100
    num0 = 0
    num1 = 1
    print (num0)

    if num0 != num_tofind:
        if num0 < limit:
            return fibonacci(num_tofind, num0 + num1, num0 +num1)
    else:

        return True


def main():
   fibonacci(21,0,1)

main()