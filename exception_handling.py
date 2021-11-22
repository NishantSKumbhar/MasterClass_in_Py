"""
@author : nishant sanjay kumbhar
@goal : to understand the concept of try and except
"""
import sys
def compare_number(num: int) -> int:
    """
    @num : number that is going to check
    """
    if type(num) != int:
        raise TypeError("Bad Type Error for num Parameter")
    if num < 0:
        raise ValueError("Bad Value For num Parameter")

    print("Hushhhhhhhhh....!")
    return num * 1


def main():
    
    try:
        compare_number(8)
    except TypeError as e:
        print("in the TypeError")
        print(e.args[0])
        # print(e.args[1])
    except ValueError as e:
        print("in the ValueError")
        print(e.args[0])
    except:
        T = sys.exc_info()
        print("Unknown Error Occurred !")
        print(T[0])
        print(T[1])
        print(T[2])
    else:
        print("this print in else part.. haaaaa :)")

main()

        
