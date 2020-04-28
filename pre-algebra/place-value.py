print("Pre algebra - Finding place value")

print("1. Find place value")
print("2. Split into face values")
print("3. Expand a number")

option = input("Enter an option:")

places = {
	0: "Ones",
	1: "Tens",
	2: "Hundreds",
	3: "Thousands",
	4: "Ten Thousands",
	5: "Hundred Thousands"
}


def find_place_value():
	number = input("Enter a number:")
	number = int(number)
	if number > 999999:
		print("Enter a number less than 999999")
		return

	digit  = input("Enter the digit you want to find place value for:")
	digit = int(digit)

	place = 0

	while number > 0:			
		if number % 10 == digit:
			print(places[place])
			break
		place += 1
		number = int(number / 10)


def split_to_face_values():
	number = input("Enter a number:")
	number = int(number)

	if number > 999999:
		print("Enter a number less than 999999")
		return

	place = 0

	while number > 0:		
		print(f"{int(number%10)} {places[place]}")
		place += 1
		number = int(number / 10)


def expand_a_number():
	number = input("Enter a number:")
	number = int(number)

	place = 0

	while number >0:
		print(number%10 * 10 ** place)
		place += 1
		number = int(number / 10)


if option == "1":
	find_place_value()
elif option == "2":
	split_to_face_values()
elif option == "3":
	expand_a_number()
else: print("Invalid option!")

