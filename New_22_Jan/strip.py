"""
@author : Nishant Sanjay Kumbhar
@goal : use of strip method
"""


a = "     Nishant Sanjay Kumbhar   "
print(a)
h = a.strip()
print(h)

l = a.lstrip()
print("L->", l)

r = a.rstrip()
print("R->", r)


# isnumeric method
k = "44444"
print(k.isnumeric())
"""
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
"""