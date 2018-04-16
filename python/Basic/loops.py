


# with open(r'C:\Users\kristhim\GitRepo\prog_ln\python\files\data','r') as f:
#     for val in f:
#         print(val)


# if __name__ == '__main__':
#     n = int(input("Enter value"))
#     if n % 2 == 0 and n > 2 and n < 6:
#         print('Not Weird')
#     elif n % 2 == 0 and n > 6 and n < 21:
#         print('Wired')
#     elif n % 2 == 0 and n > 20:
#         print('Not Wired')
#     else:
#         print('Wired')

# from itertools import *
# S, k = input().split()
# for i in permutations(S,int(k)):
#     print("".join(i))


from itertools import *
# S, k = input().split()
# for j in range(1,int(k)+1):
#     for i in combinations(sorted(S),j):
#         print("".join(i))
    
#for i ,k in groupby(map(int,list('1223433'))):

# N = int(input())
# S = input().split(' ')
# K = int(input())

# num = 0
# den = 0

# for c in combinations(S,K):
#     den+=1
#     print(c)
#     print(num)
#     num+='a' in c
       
# print (float(num)/den)


# from itertools import *

# K, M = map(int, input().split())
# N = []

# for _ in range(K):
#      N.append(map(int, input().split())[1:])        
# MAX = -1
# for i in product(*N):
#     MAX = max(sum(map(lambda x: x**2, i))%M, MAX)
    
# print(MAX)


# Sample Input

# 3
# 07895462130
# 919875641230
# 9195969878
# Sample Output

# +91 78954 62130
# +91 91959 69878
# +91 98756 41230


# n = input()
# val = []
# for _ in n:
#     val.append(input())

# def wrapper(f):
#     def fun(l):
#         result =[]
#         for v in l:
#             result.append('+91 '+v[-10:-6]+' '+v[-5:])
#         return f(result)
#     return fun

# @wrapper
# def sorted_phone(l):
#     print(l)
#     print('\n'.join(sorted(l)))

# if __name__ == '__main__':
#     val = ['07895462130','919875641230','9195969878']
#     sorted_phone(val)
# for v in val:
#     print('+91 '+v[-10:-6]+' '+v[-5:] )



# ['Mr. '+ i[0] if i[2].upper() == 'M' else 'Ms. '+i[0] for i in sorted(arr,key=lambda arr:arr[1])]
# ['Mr. kumar', 'Mr. thimma', 'Ms. lakshmi', 'Mr. krishna']