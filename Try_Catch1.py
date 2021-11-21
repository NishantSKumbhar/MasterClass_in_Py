def show(number):
    if type(number) != int:
        raise ValueError("Bad type error", 98, 66)


def main():
    print("ji")
    try:
        num = int(input("enter the number : "))
        show(num)
    except ValueError as e:
        print("type(e) : ", type(e))
        print("e.args : ", e.args)


main()
