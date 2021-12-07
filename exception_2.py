import sys
import traceback


class NegativeIntegerError(ValueError):
    pass


def factorial(n: int) -> int:
    if type(n) != int:
        raise TypeError("Bad Type for n ! ")
    if n < 0:
        raise NegativeIntegerError("Negative Integer is not Allowed ! ")

    fac = 1
    for i in range(1, n+1):
        fac = fac * i

    return fac


def main():
    num = int(input("Enter the Number : "))
    try:
        rs = factorial(num)
        print("So, The Factorial of the,", num, " is :", rs)
    except:
        print("I am in Generic Exception Handler Block")
        t = sys.exc_info()
        print(t[0])
        print(t[1])
        print(t[2])
        print(t[0].__name__)
        traceback.print_tb(t[2])
    sys.exit(0)


main()