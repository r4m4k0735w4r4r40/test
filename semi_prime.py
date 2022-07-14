import time
# def count_semi_primes(N,P,Q):
#     def arrayF(n):
#         F = [0] * (n + 1)
#         i = 2
#         while (i * i <= n):
#             if (F[i] == 0):
#                 k = i * i
#                 while (k <= n):
#                     if (F[k] == 0):
#                         F[k] = i
#                     k += i
#             i += 1
#         return F
#
#     res = arrayF(N)
#
#     def factorization(x, F):
#         primeFactors = []
#         while (F[x] > 0):
#             primeFactors += [F[x]]
#             x //= F[x]
#         primeFactors += [x]
#         return primeFactors
#
#     # print(factorization(26,res))
#     counter = [0] * (N + 1)
#     for i in range(1, N + 1):
#         result = factorization(i, res)
#         counter[i] = counter[i - 1]
#         if (len(result) == 2):
#             counter[i] += 1
#     counts = []
#     for start, end in zip(P, Q):
#         val = counter[end] - counter[start - 1]
#         counts.extend([val])
#     return counts
# N = 26
# P = [1,4,16]
# Q = [26,10,20]
# print(count_semi_primes(N,P,Q))

# def longest(s):
#     def is_valid(S):
#         nums = 0
#         strings = 0
#         flag = False
#         for i in S:
#             if (ord(i) >= ord('a') and ord(i) <= ord('z')) or (ord(i) >= ord('A') and ord(i) <= ord('Z')):
#                 strings += 1
#             elif (ord(i) >= ord('0') and ord(i) <= ord('9')):
#                 nums += 1
#             else:
#                 flag = True
#                 break
#         if flag or nums == 0 or nums % 2 == 0 or strings % 2 != 0:
#             return False
#         return True
#     s = s.split()
#     longest = -1
#     for i in s:
#         if is_valid(i) and longest < len(i):
#             longest = len(i)
#             passwd = i
#     if longest == -1:
#         return -1
#     return passwd
#
# print(longest("test 5 a0A pass007 ?xy1"))
# import time
# def gcd(a, b):
#     while True:
#         if a % b == 0:
#             return b
#         a,b = b,(a%b)
# s = time.time()
# print(gcd(51,100000000000))
# print(time.time()-s)

# Finding prime factors of a number
# def prime_factors(A,B):
#     from math import sqrt
#     def find_prime_factors(n):
#         l = set()
#         while n % 2 == 0:
#             l.add(2)
#             n = n // 2
#         for i in range(3, int(sqrt(n)) + 1, 2):
#             while n % i == 0:
#                 l.add(i)
#                 n = n // i
#         if n > 2:
#             l.add(n)
#         return l
#
#     count = 0
#     for a, b in zip(A, B):
#         if a == b:
#             count += 1
#             continue
#         maxv = max(a,b)
#         minv = min(a,b)
#         if maxv % minv != 0 or minv == 1:
#             continue
#         temp = maxv//minv
#         if temp == minv or temp % minv == 0:
#             count += 1
#             continue
#         if temp in find_prime_factors(minv):
#             count += 1
#     return count
# x = []
# y = []
# count = 0
# for i in range(1,71):
#     for k in range(1,71):
#         count += 1
#         x.append(i)
#         y.append(k)
# print(count)
# print(prime_factors(x,y))
# def array_inversion(A):
#     length = len(A)
#     count = 0
#     flag = 0
#     for i in range(length):
#         print(time.time())
#         if A[i] > 0:
#             temp = i
#             while temp < length:
#                 if A[temp] < A[i]:
#                     count += 1
#                 temp += 1
#                 if count > 1000000000:
#                     count = -1
#                     flag = 1
#                     break
#             if flag:
#                 break
#     return count
def collect_rain_water(a,n):
    for i in range(n-1,-1,-1):
        print(i)