# 2520 is the smallest number that can be divided
# by each of the numbers from 1 to 10 without any
# remainder.
#
# What is the smallest positive number that is
# evenly divisible by all of the numbers
# from 1 to 20?
n = 0
while (n<1000000000000):
    n= n + 20
    for j in range(1, 21):
        if (n%j != 0):
            break
        if (j == 20):
            print n

print ("Done")
