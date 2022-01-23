"""
@author : Nishant Sanjay Kumbhar
@goal : to hide the data from outside world
"""


"""
This program is works output -> 89
class Hide:
    num = 89
    def __init__(self):
        print(self.num)

h = Hide()
"""

"""
this also Works output -> 98
class Hide:
    __num = 89
    def __init__(self):
        print(self.__num)

h = Hide()
"""
"""
this is also works fine output -> 89 89
class Hide:
    num = 89
    def __init__(self):
        print(self.num)

h = Hide()
print(h.num)
"""
# so __ prefix is used to hide .


class Hide:
    __num = 89
    def __init__(self):
        print(self.__num)


h = Hide()
print(h.__num)

"""
output ->
89
Traceback (most recent call last):
  File "D:\Days_of_our_Life\Day1_23_jan_2022\data_hiding.py", line 46, in <module>
    print(h.__num)
AttributeError: 'Hide' object has no attribute '__num'

"""