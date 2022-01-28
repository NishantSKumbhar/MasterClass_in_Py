"""
@author : Nishant Sanjay Kumbhar
@goal : Implement Tuples
"""
name = ("Nishant", "S", "Kumbhar")
print(type(name))
print(name)
f_name, m_name, l_name = name
print(f_name)
print(m_name)
print(l_name)

l_name = []
for i in name:
    l_name.append(i)
print(l_name)
