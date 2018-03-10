from itertools import permutations
from itertools import combinations

# srclocation = ['Bangalore','Chennai','Hydrabad','Delhi','Mumbai']

# rates = [x for x in range(1000,6000,500)]

# comb = combinations(srclocation,2)

# fare = list(zip(comb,rates))
# #print(fare)

# srlloc =input("Enter your source location")
# destloc =input("Enter your destination location")
# location=(srlloc.capitalize(),destloc.capitalize())
# print(type(location))
# for val in fare:
#     if location == val[0]:
#         print("Bus fare the"+str(location[0]+' and '+location[1])+"is :"+str(val[1]))


#     print("found the location")
# perm = permutations(srclocation,2)

# count = 0
# for i in perm:
#     count +=1
#     print(i)
# print(count)


l = [1,2,3]

# comb = permutations(l)
# for i in comb:
#     print(i)


# def mycombination(it):
#     updated_list = []
#     c=1
#     for i in l:
#         tup = (l,l+1,l+2)
#         updated_list.append(tup)
#     return updated_list(tup)

# mycomb = mycombination(l)

# print(mycomb)

elements = [1,2,3]

# for perm in elements[1:]:
#     print(perm)
#     # for i in range(len(elements)):
#     #     print(perm[:i] + elements[0:1])

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            print(perm)
            # for i in range(len(elements)):
            #     #print(i)
            #     # nb elements[0:1] works in both string and list contexts
            #     print(perm[:i] + elements[0:1]+perm[i:])
            #     yield perm[:i] + elements[0:1] + perm[i:]

# all = all_perms(elements)
# for i in all:
#     print(i)