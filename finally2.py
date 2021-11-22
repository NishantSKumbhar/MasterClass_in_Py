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
    print(x)
    return num * 1


def main():
    
    try:
        compare_number(5)
    except TypeError as e:
        print("in the TypeError")
        print(e.args[0])
        # print(e.args[1])
    except ValueError as e:
        print("in the ValueError")
        print(e.args[0])    
    finally:
        # this part exicute whatever it takes.
        # e.g if we open file i.e f.open() and because of exception program
        # terminate abnormally then we will miss to close the file i.e f.close()
        # so we write f.close() command in finally block
        print("F I N A L")

    print("This will be not printed, if due to exception progran is going to terminate.")

main()

        
