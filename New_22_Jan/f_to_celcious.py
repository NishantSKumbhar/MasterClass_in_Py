"""
@author : Nishant Sanjay Kumbhar
@goal : 0 to 100 f convert to degree celcious
"""


def to_celsius(x):
    return (x - 31) * 5/9


for x in range(100):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))  # > sign for right and next number are spaces

    # :.2f  that means 2 decimal spaces
    # :>3   that means three right spaces
    # :>6.2 that means six right spaces and 2 decimal point
