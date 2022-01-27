"""
@author : Nishant Sanjay Kumbhar
@goal : Explain the format string
"""
a = "NishantSKumbhar"
print("{}".format(a))

print("{:}".format(a))

print("{:1}".format(a))

print("{:.1}".format(a))
print("{:.2}".format(a))
print("{:.7}".format(a))
print("{:.15}".format(a))

a = 45678.1234
print("\n{}".format(a))

print("{:}".format(a))

print("{:1}".format(a))

print("{:.1}".format(a))

print("{:.1f}".format(a))
print("{:.2f}".format(a))
print("{:.3f}".format(a))
print("{:.4f}".format(a))

print("{:15.3f}".format(a))
print("{:>15.3f}".format(a))
print("{:<15.3f}".format(a))

for i in range(1001):
    print("{:>3}".format(i))