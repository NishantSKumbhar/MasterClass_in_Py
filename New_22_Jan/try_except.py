"""
@author : Nishant Sanjay Kumbhar
@goal : try and block universal.
"""
import sys


def factorial(num: int) -> int:
    fac = 1
    if type(num) != int:
        raise TypeError("Bad Type for Factorial Number.")
    if num < 0:
        raise ValueError("Bad Value for Factorial Number")
    if num == 0:
        return 1
    for i in range(1, num+1):
        fac *= i
    return fac


def main():

    try:
        number = int(input("Enter the Number for Factorial : "))
        f = factorial(number)
        print(f"Factorial of {number} is {f}.")
    except:
        print("I am in Generic Exception Handler.")
        t = sys.exc_info()
        print(t[0])
        print(t[0].__name__)
        print(t[1])
        print(t[2])

main()