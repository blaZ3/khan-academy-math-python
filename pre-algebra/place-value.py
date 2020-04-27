print("Pre algebra - Finding place value")

print("1. Find place value")
print("2. Split into face values")

option = input("Enter an option:")

places = {
	1: "Ones",
	2: "Tens",
	3: "Hundreds",
	4: "Thousands",
	5: "Ten Thousands",
	6: "Hundred Thousands"
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
		place += 1
		if number % 10 == digit:
			print(places[place])
			break
		number = int(number / 10)


def split_to_face_values():
	number = input("Enter a number:")
	number = int(number)

	if number > 999999:
		print("Enter a number less than 999999")
		return

	place = 0

	while number > 0:
		place += 1
		print(f"{int(number%10)} {places[place]}")
		number = int(number / 10)


if option == "1":
	find_place_value()
elif option == "2":
	split_to_face_values()
else: print("Invalid option!")


