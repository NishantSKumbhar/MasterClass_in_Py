"""
@author : Nishant Sanjay Kumbhar
@goal : see the assert keyword how to use it.
"""


def main():
    numerator = int(input("Enter the Numerator : "))
    denominator = int(input("Enter the Denominator : "))
    assert denominator != 0, "Denominator should not be zero"
    result = numerator / denominator
    print(result)


main()
