#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1] if number > 0 else "-" + (str(number)[-1])
first_str = f"Last digit of {number} is {last_digit}" 
if int(last_digit) > 5: 
    print(f"{first_str} and is greater than 5")
elif int(last_digit) == 0:
    print(f"{first_str} and is 0")
else:
    print(f"{first_str} snd is less than 6 and not 0")
