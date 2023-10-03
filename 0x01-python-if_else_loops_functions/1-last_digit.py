#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number
while last > 9:
    last = number % 10
if last == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif 0 < last < 6:
    print(f"Last digit of {number} is {last} and and is less than 6 and not 0")
