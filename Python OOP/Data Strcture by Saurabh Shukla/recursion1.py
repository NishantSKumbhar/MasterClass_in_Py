def sum_of(number):
	if number == 1:
		return number

	addition = number + sum_of(number - 1)
	return addition


def main():
	n = 10
	s = sum_of(n)
	print(f"Sum of {n} numbers : {s}")


main()