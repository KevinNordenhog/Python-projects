# A palindromic number reads the same both ways.
# The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product
# of two 3-digit numbers.

def isPalindrom(n):
    s = str(n)
    if (s == (s[::-1])):
        return True
    else:
        return False

temp = 0
for i in range(1, 1000):
    for j in range(1, 1000):
        if (isPalindrom(i*j) and ((i*j)>temp)):
            temp = i*j


print temp
