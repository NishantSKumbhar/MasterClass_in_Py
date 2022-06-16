def sample_function(num1, num2):
    if num1 == num2:
        return True
    else:
        return False


if sample_function(1, 4):
    print("Yes Equal !")
else:
    print("NOt Equal !")

print(sample_function.__code__)
print(dir(sample_function.__code__))

"""
First Headers Compiles and Convert them in machine Code and store this in Object called Code.
This Code Object is Stored in the Object called Function Object.
Function Object is then Bind with the Respective Function
"""

print('*' * 30)

print(f"Start : Global ---> {globals()}")
def outer():
    print("Entered in Outer !")
    n = 10
    v = 89
    print(f"start outer local : {locals()}")
    def inner():
        print(f"start inner : {locals()}")
        print("Entered in Inner !")
        print(f"Value of N : {n}")    # Implicit State Saving
    print("Outer End !")
    print(f"End outer : {locals()}")
    return inner

print(f"End : Global ---> {globals()}")
x = outer()
print(f"END End : Global ---> {globals()}")
x()
