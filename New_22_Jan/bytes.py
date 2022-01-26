""""
If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte
will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage.
 Knowing this, can you fill in the gaps in the calculate_storage function below,
 which calculates the total number of bytes needed to store a file of a given size?
"""

"""
def format_name(first_name, last_name):
	# code goes here
	if first_name and last_name:
		string = str(first_name) + " , " + str(last_name)
	elif first_name:
		string = str(first_name)
	elif last_name:
		string = str(last_name)
	else:
		string = ""
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
"""

"""
Question 10

The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number.
Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.
def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
	if denominator == 0:
		return 0
	else:
		div = numerator / denominator
		frac = div % 1
		return frac
print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
"""

"""
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT
"""

"""
def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n != 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
"""

"""
def sum_divisors(n):
  sum = 0
  # Return the sum of all divisors of n, not including n
  if n > 0:
    i = 1
    while(i < n):
      if n%i == 0:
        sum += i
      i += 1

  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

"""
"""def square(n):
    return n*n


def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum


print(sum_squares(10))
"""

"""


def count_users(group):
    count = 0
    for member in get_members(group):
    #count += 1
        if is_group(member):
            count += count_users(member)
        else:
            count+=1
    return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18


"""

"""
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  number = number / base
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return False
  else:
    return True
  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
"""

"""
def count_users(group):
    count = 0
    for member in get_members(group):
    #count += 1
        if is_group(member):
            count += count_users(member)
        else:
            count+=1
    return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18

"""

"""
def digits(n):
    count = 0
    if n == 0:
        return 1
    while (n != 0):
        count += 1
        n = n // 10
    return count


print(digits(25))  # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))  # Should print 1
"""

"""
def multiplication_table(start, stop):
	for x in range(start, stop+1):
		for y in range(1, stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above
"""


"""
def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x -= 1
			
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x += 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
"""

for x in range(10):
    for y in range(x):
        print(y)