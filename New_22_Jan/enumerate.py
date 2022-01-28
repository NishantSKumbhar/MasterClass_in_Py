"""
@author : Nishant Sanjay Kumbhar
@goal : see the enumerate how it works
"""
# enumerate return the index and element or character in tuple.

list = ["Red", "Blue", "Violet", "Pink", "Blue"]
for index, clr in enumerate(list):
    print(f"{index + 1} : {clr}")


def skip_elements(elements):
    # code goes here
    final = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            final.append(element)

    return final


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']
