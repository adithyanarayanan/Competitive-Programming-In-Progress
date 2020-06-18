#PRIME1 - UNSOLVED- Time Limit Exceeded
#Status: Solution works, but not accepted- May need Big integer equivalent

"""
Print all prime numbers between two given limits
Problem: https://www.spoj.com/problems/PRIME1/
"""



def print_primes(m,n):
    primes = []

    for i in range(2,n+1):
        if i == 2:
            primes.append(i)
            if i >= m:
                print(i)
            continue

        flag = True
        for j in primes:
            if i%j == 0:
                flag = False

        if flag:
            primes.append(i)

            if i >= m:
                print(i)



t = int(input())

q = 0
while q < t:
    q += 1
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    print_primes(m,n)
