# def alph_rangoli(n):
#     tot = ((n-1)*4)+1
#     l = []
#     letters = ''
#     for i in range(97,(97+n)):
#         letters += chr(i)
#     x = -1
#     for i in range(n):
#         st = ''
#         j = -1
#         while j != x:
#             st += "{}-".format(letters[j])
#             j += -1
#         st = st + letters[j]+st[::-1]
#         st = str.center(st,tot,'-')
#         l.append(st)
#         x += -1
#     print(l,'\n')
#     for i in range(n):
#         print(l[i])
#     for i in range(n-2,-1,-1):
#         print(l[i])
# alph_rangoli(26)

# def minion_game(string):
#     string.upper()
#     length = len(string)
#     l = []
#     def is_vowel(c):
#         if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
#             return True
#         return False
#     for i in range(length):
#         for j in range(i,length):
#             l.append(string[i:j+1])
#     print(l)
#     l_set = set(l)
#     kevin = 0
#     stuart = 0
#     for i in l_set:
#         temp = l.count(i)
#         if is_vowel(i[0]):
#             kevin += temp
#             continue
#         stuart += temp
#         print(i)
#     if kevin > stuart:
#         print('Kevin {}'.format(kevin))
#     else:
#         print('Stuart {}'.format(stuart))
# minion_game('BANANA')
# print("APPLE")
# l = set()
# # for i in range(ord('0'),ord('9')+1):
# #     l.add(chr(i))
# # print(l)
# a = {1,34,23,78,231,66,21,42,78,23,67}
# from cmath import phase
# from math import sqrt
# z = complex(input())
# real = z.real
# img = z.imag
# print(sqrt((real**2)+(img**2)))
# def average(array):
#     array = set(array)
#     length = len(array)
#     sums = sum(array)
#     avg = float("{:.3f}".format(sums / length))
#     return avg
# a = '161 182 161 154 176 170 167 171 170 174'
# arr = list(map(int, a.split()))
# result = average(arr)
# print(result)
# from collections import defaultdict
# def solution(a,b):
#     dic = defaultdict(list)
#     for i in enumerate(a):
#         dic[i[1]].append(i[0])
#     for i in b:
#         if dic[i] == []:
#             print(-1)
#         else:
#             print(*dic[i])
#
# x = list(map(int,input().split(" ")))
# n,m = x[0],x[1]
# a = []
# b = []
# for i in range(n+m):
#     temp = input()
#     if i < n:
#         a.append(temp)
#     else:
#         b.append(temp)
# solution(a, b)
# import calendar
# def solution(d,m,y):
#     day = calendar.weekday(y,m,d)
#     return (calendar.day_name[day]).upper()
# date = list(map(int,input().split(" ")))
# print(solution(date[1],date[0],date[2]))

# def solution(a,b):
#     try:
#         return int(a)//int(b)
#     except Exception as e:
#         return "Error Code:{}".format(e)
# n = int(input())
# l = []
# for _ in range(n):
#     temp = input().split(" ")
#     l.append(temp)
# for i in l:
#     print(solution(*i))
# from collections import namedtuple
# n = int(input())
# header = input().split()
# student = namedtuple('Student',header)
# count = 0
# for _ in range(n):
#     temp = input().split()
#     st = student(*temp)
#     count += int(st.MARKS)
# print(count/5)

# n = int(input())
# co_dic = {}
# for _ in range(n):
#     temp = input().split()
#     key = " ".join(temp[0:-1])
#     val = int(temp[-1])
#     if key in co_dic:
#         co_dic[key] += val
#     else:
#         co_dic[key] = val
# for key,val in co_dic.items():
#     print("{} {}".format(key,val))

# a = set([1,2,3,4,5,6,7])
# b = set([3,4,5,6,7,8,9])
# c = a.symmetric_difference(b)
# print(c,a,b)
# def inter_update(b):
#     a.intersection_update(b)
# def symmmet_diff_update(b):
#     a.symmetric_difference_update(b)
# def set_update(b):
#     a.difference_update(b)
# def diff_update(b):
#     a.update(b)
# n = int(input())
# a = set(map(int,input().split()))
# m = int(input())
# l = []
# for i in range(1,(2*m)+1):
#     l.append(input().split())
#     if i % 2 == 0:
#         b = set(map(int,l[1]))
#         if l[0][0] == "intersection_update":
#             inter_update(b)
#         if l[0][0] == "symmetric_difference_update":
#             symmmet_diff_update(b)
#         if l[0][0] == "update":
#             set_update(b)
#         if l[0][0] == "difference_update":
#             diff_update(b)
#         l = []
#         print(a)
# print(sum(a))

# n = int(input())
# arr = list(map(int,input.split()))
# dic = {}
# for i in arr:
#     if i in dic:
#         dic[i] += 1
#         continue
#     dic[i] = 1
# for key,val in dic.items():
#     if val == 1:
#         break
# print(key)
# x = list(map(int,input().split()))
# studs = x[0]
# subs = x[1]
# a = []
# for _ in range(subs):
#     temp = list(map(float,input().split()))
#     a.append(temp)
# print(a)
# print(zip(*a))

# def timeconversion(s):
#     temp = s
#     s = s.split(":")
#     print(s)
#     print(s[2][2:4])
#     if s[2][2:4] == 'AM' and int(s[0]) != 12:
#         return temp[0:-2]
#     if s[2][2:4] == 'PM' and int(s[0]) == 12:
#         return temp[0:-2]
#     elif s[2][2:4] == 'AM':
#         s[2] = s[2][0:-2]
#         s[0] = '00'
#     else:
#         s[2] = s[2][0:-2]
#         s[0] = str(12 + int(s[0]))
#     return ':'.join(s)
# print(timeconversion('12:40:22AM'))

# from collections import Counter as counter

# a = [1,2,3,4,5,4,6,4,3,5,6,7,3,2,4,5,6,7,8,5,3,7]
# c = counter(a)
# c[2] -= 1
# print(c)
# a = set(map(int,input().split()))
# n = int(input())
# import re
# pattern = r'[a-z0-9]+@[a-z]+.[a-z]+'
# print(pattern)
# a = 'abcdhjghdjhfgudhg54689756gfhgjdfhdgdbu9@gmail.com'
# match = re.match(pattern,a)
# print(match)
# def samp(func,n):
#     return func(n)
# print(type(samp(int,'1')))

from String import String
st = String('ddsfsdag')
# st1 = String('fafae')
print(st)
# print(st[0:3])
# print(st)
# st.setTo('ygrfrhsgufyguyguyrgt')
st.update(0,'A')
print(st)
# st.remove(0)
# print(st)
# st.pop()
# print(st)
# st.append('ghsduyrt')
# print(st)
# print(len(st))

# number = Number(10000000)
# print(len(number))
