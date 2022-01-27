"""
@author : Nishant Sanjay Kumbhar
@goal : use f in decimal point
"""

tax = 84.5543
gst = 9.7
print(f"So the Tax will be {tax} and gst will be {gst} ")
print("So the Tax will be {} and gst will be {}".format(tax, gst))

# now game changer
print("So the Tax will be {:.2f} and gst will be {:.2f}".format(tax, gst))
