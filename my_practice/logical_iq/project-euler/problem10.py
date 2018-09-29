def isPrime(n):

    if n%2 == 0:
        return False
    for i in range(3,n,2):
        if n%i == 0:
            return False 
    return True

prime = []
for i in range(1,2000000):
    if i == 1:
        prime.append(i)
    elif i == 2:
        prime.append(i)
    elif isPrime(i):
        prime.append(i)
    else:
        pass

print(sum(prime))
