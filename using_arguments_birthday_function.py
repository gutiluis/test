# calculate the birthday using other functions
def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b


birth_year = int(input("Enter you birth year: "))
current_year = int(input("Enter the current year: "))


print(f"{birth_year}, {current_year}")


oper = current_year - birth_year
print("Result", oper)