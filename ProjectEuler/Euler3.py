# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def isPrime(p):
    for i in range(2,(p/2)+1):
        if (p%i == 0):
            return False
            # print ("False")
    return True
    # print ("True")

prime = []
n = 0
count = 0
for j in range(2,10000):
    if(isPrime(j)):
        prime.insert(n, j)
        n = n + 1


for k in range(n-1,1,-1):
    if(600851475143%prime[k]==0):
        print prime[k]


# # Tests isPrime
# for j in range (2,100):
#     if (isPrime(j)):
#         print j

# for j in range(600851475143, 2, -1):
#     if (600851475143%j==0):
#         if(isPrime(j)):
#             print j
#             break
