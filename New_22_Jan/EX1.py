"""
@author : Nishant Sanjay Kumbhar
@goal : user input 1 -> 26
        user input 2 -> 6

            then ->   26          print  ->-> 26
                      26*26                 -> 676
                      26*26*26               -> 17576
                      .
                      .
                      .
                      26*26*26*26*26*26         -> 6156119580207157310796674288400203776
"""
import sys


def main():
    num = int(input("Enter the Number i.e model -> "))
    it = int(input("Enter the count till iterate : "))
    flag = num
    for i in range(it):
        ans = flag
        for j in range(i):
            ans *= num
        print(ans)


main()
