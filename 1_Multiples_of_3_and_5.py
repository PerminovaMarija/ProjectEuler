"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

mult_3_or_5 = []
for number in range(1000):
    if number % 3 == 0 or number % 5 == 0:
        mult_3_or_5.append(number)
print(sum(mult_3_or_5))

