#!/usr/bin/env python3

number = int(input("Choose a number: "))
steps = 0

for i in range(1000):
	if number == 1:
		break
	elif number % 2 == 0:
		number = number / 2
		steps = steps + 1
	else:
		number = (number * 3) + 1
		steps = steps + 1

if number == 1:
	print ("It took ",steps," to reach number 1")
else:
	print("Number did not reach 1")
