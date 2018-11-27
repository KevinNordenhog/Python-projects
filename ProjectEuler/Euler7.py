# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

def isPrime(p):
    for i in range(2,(p/2)+1):
        if (p%i == 0):
            return False
            # print ("False")
    return True

n = 0
k = 1
while (n<10001):
    k = k + 1
    if (isPrime(k)):
        n = n + 1


print k
