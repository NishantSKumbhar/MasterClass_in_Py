"""
@author : Nishant Sanjay Kumbhar
@goal : change the extension of list of files.
"""
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for i in filenames:
    new_list = i.split('.')
    if new_list[-1] == 'c' or new_list[-1] == 'out':
        newfilenames.append(i)
    elif new_list[-1] == 'hpp':
        new_list[-1] = '.h'
        newfilenames.append(new_list[0] + new_list[1])

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
