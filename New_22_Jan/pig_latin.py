"""
@author : Nishant Sanjay Kumbhar
@goal : convert string to pig-latin string
"""


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for i in words:
        em_list = []
        for j in i:
            em_list.append(j)
        em_list.append(em_list[0])
        em_list.pop(0)
        em_list.append("ay")
        for k in em_list:
            say = say + k
        if i != words[-1]:
            say = say + " "

    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"
