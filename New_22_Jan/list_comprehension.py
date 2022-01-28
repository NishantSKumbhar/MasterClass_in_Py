""""
@author : Nishant Sanjay Kumbhar
@goal : list comprehension
"""
empt_list = []
for x in range(1, 11):
    empt_list.append(x*8)

print(empt_list)

# now using list comprehension
demo_list = [x*8 for x in range(1, 11)]
print(demo_list)

languages = ["Python", "Ruby", "Perl", "Go", "Java", "C", "C++"]
len_list = [len(x) for x in languages]
print(len_list)

divisible = [x for x in range(1, 100) if x%3 == 0]
print(divisible)


number = int(input("Enter the Number : "))
list_of_odd = [x for x in range(1, number+1) if x%2 != 0]
print(list_of_odd)
