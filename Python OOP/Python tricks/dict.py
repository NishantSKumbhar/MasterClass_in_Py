ages = {
	'Ramesh' : 34,
	'Suresh' : 23,
	'Mohan' : 20
}

age = ages.get('Radha', 'Unknown')
print(f"Radha is {age} years old !")
# does not affect the orgnal dict.
print(ages)