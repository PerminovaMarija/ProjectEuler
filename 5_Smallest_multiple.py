"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

n = 20

start = True
while start == True:
    a = True
    for i in range(1, 21):
        if n % i != 0:
            a = False
    if a == True:
        print(n)
        start = False
    else:
        n += 20













