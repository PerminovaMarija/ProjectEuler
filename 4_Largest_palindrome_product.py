"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

max = 998001
list_a = []

for x in range(100, 1000):
    a = 1000
    while a >= 100:
        pal = x*a
        if str(pal) == str(pal)[::-1]:
            list_a.append(pal)
        a -= 1
print((sorted(list_a))[-1])


list_b = []
for x in range(100, 1000):
    for a in range(100, 1000):
        if str(x*a) == str(x*a)[::-1]:
            list_b.append(x*a)
print(sorted(list_b)[-1])

