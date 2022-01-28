"""
@author : Nishant Sanjay Kumbhar
@goal : Separate the name from E-mail in format -> Nishant <nish.kumbhar02@gmail.com>
"""


def separate(obj: tuple) -> list:
    temp_list = []
    for name, mail in obj:
        temp_list.append("{} <{}>".format(name, mail))
    return temp_list


#print(separate([("Nishant", "nishantsk210@gmail.com"), ("Shubham", "shubhamkd567@gmail.com")]))
print(separate(("Nishant", "nishantsk210@gmail.com")))