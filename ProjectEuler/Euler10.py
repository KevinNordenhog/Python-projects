# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# USING my version of sieve of Eratosthenes principle

target = 2000000
#List comprehension
prim = [x for x in range(2,target)]

# print target**(0.5)        //=== 44.72
# print int(target**(0.5))   //=== 44
for i in range(2, int(target**(0.5))):
    for j in range(i ** 2, target, i):
        # del prim[j-2]                          #del tar bort elementet och forsjuter listan....
        prim[j-2] = 0

# print prim   # it works
s = sum(prim)
print s



















#
# def isPrime(p):
#     for i in range(2,(p/2)+1):
#         if (p%i == 0):
#             return False
#     return True
#
# prime = [2, 3, 5]
# # test
# # prime.insert(1, 3)
# n = 3
# # for j in range(3,2000000,2):
# #     if ((j%3 != 0) and (j%5 != 0) and (j%7 != 0)):
# #         if(isPrime(j)):
# #             prime.insert(n, j)
# #             n = n + 1
#
# for j in range(3,2000000,2):
#     b= True
#     for k in range(0, len(prime)):
#         if (j%prime[k] == 0):
#             b = False
#             break
#     if(b):
# #        if (isPrime(j)):
#             prime.insert(n, j)
#             n = n + 1
#
#
# s = sum(prime)
# print s
# # print prime



#  isPrime works!
# for j in range(2, 1000):
#     if (isPrime(j)):
#         print j
