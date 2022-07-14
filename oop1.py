# class String(str):
#     def __add__(self, other):
#         s = str.__repr__(self)
#         s = s[1:-1]
#         return s*other
#     def sort(self):
#         s = str.__repr__(self)
#         l = list(s)
#         l.sort()
#         return ''.join(l)
# s = String('JDSDJGSDLG')
# print(s.upper())
#

# import sys
# print(sys.getrecursionlimit())
# print(sys.setrecursionlimit(100))
# def fib(n,a=0,b=1,c=2):
#     if c < n-1:
#         yield a + b
#         yield from fib(n, b, a + b, c + 1)
#     else:
#         yield a+b
# print(0,1,end=' ')
# for i in fib(5):
#     print(i,end=' ')

import random
l = ''
for _ in range(1000000):
    temp = '{} '.format(random.randint(0,9))
    l += temp
with open('test.txt','w') as fd:
    fd.write(l)
print('Comleted')