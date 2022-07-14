import itertools
#a = int(input('Enter number:'))
#match a:
#    case 0:
#        print(0)
#    case 1:
#        print(1)
#    case 2:
#        print(2)
#    case default:
#        print("No match")

# A = [3,4,4,6,1,4,4]
# N = 5
# count = [0]*N
# for i in A:
#     if(i == N+1):
#         count = [max(count)]*N
#     else:
#         count[i - 1] += 1
# print(count)
# a = [0, 1, 0, 1, 1]
# length = len(a)
# count = 0
# for i in range(length):
#     for el in a[i+1:]:
#         if el == 1 and a[i] == 0:
#             print(el, a[i])
#             count += 1
        # elif el == 0 and a[i] ==1:
        #     print(el, a[i])
        #     count += 1
# return count
# print(count)
# S = 'CAGCCTA'
# P = [2, 5, 0]
# Q = [4, 5, 6]
# length = len(P)
# length2 = len(S)
# S = list(S)
# impact = [0] * length
# dic = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
# for i in range(length):
#     print(abs(P[i] - Q[i]))
#     if (abs(P[i] - Q[i]) == length2 - 1):
#         impact[i] = 1
#         continue
#     temp = S[P[i]:Q[i] + 1]
#     temp.sort()
#     impact[i] = dic[temp[0]]
# print(impact)

a = [1,1,1,1,1,2,3,4,5]
# a = [3, 4, 3, 2, 3, -1, 3]
a = [1,2,1,3,1,4,1,5,1,6,1]
a = [4,3,4,4,4,2]
length = len(a)
# def find_leader(a):
#     length = len(a)
#     # print(length)
#     # print(a.count(1))
#     size = 0
#     for i in a:
#         if size == 0:
#             size += 1
#             value = i
#         else:
#             if i != value:
#                 size -= 1
#             else:
#                 size += 1
#     # print(size)
#     if (size != 0 and length // 2 < a.count(value)):
#         return [1,value]
#     else:
#         return [0]

# def check_par(s):
#     length = len(s)
#     char_stack = [0] * length
#     size = 0
#     dic = {'}': '{', ')': '(', ']': '['}
#     for i in s:
#         if (i == '{' or i == '(' or i == '['):
#             char_stack[size] = i
#             size += 1
#             continue
#         open_par = dic[i]
#         size -= 1
#         if (char_stack[size] != open_par):
#             return 0
#     if size == 0:
#         return 1
#     return 0
# s = '{[)()]}'
# print(check_par(s))

# def inersect_pairs(a):
#     max_limit = 10000000
#     left =[]
#     right = []
#     for p,r in enumerate(a):
#         left.append(p-r)
#         right.append(p+r)
#     print(left, right)
#     left.sort()
#     right.sort()
#     print(left,right)
#     length = len(left)
#     count = left_start = 0
#     for i in range(length):
#         while left_start < length and left[left_start] < right[i]:
#             left_start += 1
#         print(left_start,i,(left_start-i-1))
#         count += left_start-i-1
#         if count > max_limit:
#             return -1
#     return count
#
# a = [1,5,2,1,4,0]
# print(inersect_pairs(a))

# def live_fish(a,b):
#     length = len(a)
#     fish_stack = []
#     escaped = 0
#     for i in range(length):
#         if b[i] == 0:
#             if fish_stack:
#                 while fish_stack and fish_stack[-1] < a[i]:
#                     fish_stack.pop()
#                 if not fish_stack:
#                     escaped += 1
#             else:
#                 escaped += 1
#         else:
#             fish_stack.append(a[i])
#     return escaped + len(fish_stack)
#
# a = [4,3,2,1,5]
# b = [0,1,0,0,0]
# print(live_fish(a,b))

# def no_of_blocks(a):
#     height_stack = []
#     blocks_count = 0
#     for i in range(len(a)):
#         while height_stack and height_stack[-1] > a[i]:
#             height_stack.pop()
#         if not height_stack or height_stack[-1] < a[i]:
#             height_stack.append(a[i])
#             blocks_count += 1
#     return blocks_count
# a = [8,5,7,9,8,7,4,8]
# print(a)
# print(no_of_blocks(a))

# def small_perimeter(N):
#     import math
#     def find_parameter(l, b):
#         return 2 * (l + b)
#
#     small = find_parameter(1, N)
#     for i in range(2, int(math.sqrt(N))):
#         if (N % i == 0):
#             temp = find_parameter(i, N // i)
#             if (small > temp):
#                 small = temp
#     return small
# print(small_perimeter(30))

# def no_of_facts(N):
#     import math
#     count = 0
#     for i in range(1, int(math.sqrt(N)) + 1):
#         if (N % i == 0):
#             if(N//i == i):
#                 count += 1
#             else:
#                 count += 2
#     return count
# print(no_of_facts(36))

# def eqilibrium(a):
#     left_sum = 0
#     right_sum = sum(a)
#     small = right_sum
#     print(small)
#     for i in a:
#         left_sum += i
#         right_sum -= i
#         temp = abs(left_sum - right_sum)
#         if temp < small:
#             small = temp
#     return small
#
# a = [3,1,2,4,3]
# # a = [1, 1, 3]
# a = [-1000,1000]
# print(eqilibrium(a))

# def slow_max_slice(A):
#     n = len(A)
#     result = 0
#     l = []
#     for p in range(n):
#         for q in range(p+1, n):
#             sum = 0
#             for i in range(p, q + 1):
#                 print(A[i],end=' ')
#                 sum += A[i]
#             print('\n')
#             l.append(sum)
#             result = max(result, sum)
#     max_ending = max_slice = 0
#     for a in A:
#         max_ending = max(0, max_ending + a)
#         max_slice = max(max_slice, max_ending)
#     print(max_slice)
#     print(l)
#     return result
# def max_sli
# a = [5,-7,3,5,-2,4,-1]
# a = [3, 2, -6, 4, 0]
# print(slow_max_slice(a))

# def odd_occur(a):
#     length = len(a)
#     if length == 0:
#         return 0
#     if length == 1:
#         return a[0]
#     result = 0
#     for i in a:
#
#     return result
# a = [9,3,9,3,9,7,9]
# print(odd_occur(a))

# def sieve(n):
#     sieve = [True] * (n+1)
#     sieve[0] = sieve[1] = False
#     i = 2
#     while (i * i <= n):
#         if (sieve[i]):
#             k = i * i
#             while (k <= n):
#                 sieve[k] = False
#                 k += i
#         i += 1
#     return sieve
# print(sieve(19))

# def peak(A):
#     length = len(A)
#     if length < 3:
#         return 0
#     peaks = [0] * length
#     for index in range(2, length):
#         peaks[index] = peaks[index - 1]
#         if A[index - 1] > A[index - 2] and A[index - 1] > A[index]:
#             peaks[index] += 1
#     for candidate in range(3, length + 1):
#         if length % candidate != 0:
#             continue
#         valid = True
#         print(candidate)
#         index = candidate
#         while index != length:
#             if peaks[index] == peaks[index - candidate]:
#                 valid = False
#                 break
#             index += candidate
#         if index == length and peaks[index - 1] == peaks[index - candidate]:
#             valid = False
#         if valid:
#             return length // candidate
#     return 0
# a = [1,5,3,4,3,4,1,2,3,4,6,2]
# print(peak(a))

vins_list = ['A123', 'B123']
batch_keys = {
'order_data_test': {
'Keys': [{'vinLong': {'S': vin}} for vin in vins_list], #modify list Comprehension
'AttributesToGet': ['vinLong', 'bodyType']
}
}



# print(batch_keys)
#{'order_data_test': {'Keys': [{'vinLong': {'S': 'A123'}}, {'vinLong': {'S': 'B123'}}], 'AttributesToGet': ['vinLong', 'bodyType']}}
#{'order_data_test': {'Keys': [{'vinLong': {'S': 'A123'}}, {'vinLong': {'S': 'B123'}}], 'AttributesToGet': ['vinLong', 'bodyType']}}

def extract_values(dic,l):
    for key,value in dic.items():
        if type(value) is dict:
            extract_values(value,l)
        else:
            l.append(value)
# dic = [{'vinLong': {'S': 'a123'}}, {'vinLong': {'S': 'b123'}}]
# l = []
# for i in dic:
#     extract_values(i,l)
# print(l)

# list1 = ['a123', 'b123', 'c123']
# list2 = ['a123', 'b123','d']
#
# diff1 = list(set(list1)-set(list2))
# diff2 = list(set(list2)-set(list1))
# print(diff1+diff2)
# import math
# def check(n):
#     for i in range(1,int(math.sqrt(n))+1):
#         if n % i == 0:
#             print(i,n//i,end=' ')
# check(36)

def frog(X,A):
    length = len(A)
    if length < X:
        return -1
    total = (X * (X + 1)) // 2
    count = [0] * (X + 1)
    for i in range(length):
        count[A[i]] += 1
        if (count[A[i]] == 1):
            total -= A[i]
        if total == 0:
            return i
    return -1
# a = [1, 3, 1, 4, 2, 3, 5, 4]
# print(frog(5,a))
# a = True
# a = not a
# print(a)

# def max_slice(a):
#     max_include = 0
#     max_value = -1000001
#     for i in a:
#         max_include = max(max_include,max_include+i)
#         max_value = max(max_include,max_value)
#     return max_value
# a = [3,2,-6,4,0]
# print(max_slice(a))
# import time
# def cout_chocs(N,M):
#     if N == 1:
#         return 1
#     i = N
#     count = 1
#     while True:
#         rem = i % M
#         if rem == 0:
#             count = i//M
#             break
#         i += N
#     return count
# print(cout_chocs(2, 1000000000))

# def parking_cost(E,L):
#     def convert_int(T):
#         T = list(map(int, T.split(':')))
#         return T
#     E = convert_int(E)
#     L = convert_int(L)
#     cost = 2
#     diff = [(L[0]-E[0]),(L[1]-E[1])]
#     print(diff)
#     if diff[0] == 0:
#         return cost+3
#     if diff[0] >= 1:
#         cost += 3
#     cost += (diff[0]-1)*4
#     if diff[1] <= 0:
#         return cost
#     return cost+4
# print(parking_cost('21:53', '22:48'))

# def three_letters(A,B):
#     if A == B:
#         return 'ab'*A
#     if A // 2 <= B:
#         i = 0
#         j = 0
#         st = ''
#         while i <= A:
#             st += 'aab'
#             i += 2
#             j += 1
#         i = A-(i-2)
#         j = B-(j-1)
#         st += (('a'*i)+('b'*j))
#         return st[3:]
#
# print(three_letters(7,6))
def fib_frog(A):
    def find_fib(n):
        a = (1 + 2.23606797749979)/2
        return round((a**n)/2.23606797749979)
    fibs = []
    length = len(A)
    if length == 0 or length == 1 or length == 2:
        return 1
    i = 0
    while True:
        fib = find_fib(i)
        if fib == length + 1:
            print(1)
            return 1
        if fib == length and (A[fib-1] == 1 or A[0] == 1):
            print(2)
            return 2
        if fib > length:
            break
        fibs.append(fib)
        i += 1
    fib_i = i - 1
    print(fibs)
    i = fib_i
    pos = -1
    count = 0
    while True:
        if i < 0:
            return -1
        temp = fibs[i] + pos
        if temp == length:
            print(3)
            return count + 1
        if temp == length - 1 and A[temp] == 1:
            print(4)
            return count + 2
        if temp < length and temp > pos:
            if A[temp] == 1:
                count += 1
                i = fib_i
                pos = temp
        print(temp,pos,i)
        i -= 1
a = [0, 1, 0, 1, 0]
# print(len(a))
# print(fib_frog(a))

# def second_max(arr):
#     max1 = arr[0]
#     max2 = arr[0]
#     for i in arr:
#         if i > max1:
#             max2 = max1
#             max1 = i
#         if i > max2 and i < max1:
#             max2 = i
#     return max2
# a = [5,1,3,9,6,4,7,9,0,2,45,67,3242,7897,2342,4435,3213,123,98,121,433]
# a = [1,4,12,12,7]
# print(second_max(a))

def dist_slices(M,A):
    def all_dists(n):
        n = (n*(n+1))//2
        return n
    length = len(A)
    if length == 0:
        return 0
    nums = [0]*M
    count = length
    i = 0
    j = 0
    while i < length:
        if nums[A[i]] == 0:
            nums[A[i]] += 1
            j += 1
        else:
            nums = [0] * M
            count += all_dists(j-1)
            if count > 1000000000:
                return 1000000000
            nums[A[i]] += 1
            j = 1
        i += 1
    count += all_dists(j - 1)
    if count > 1000000000:
        return 1000000000
    return count
# A = [3,4,5,5,2]
M = 6
A = 0, [0]
print(dist_slices(M,A))

