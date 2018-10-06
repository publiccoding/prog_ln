a = '1'
b = ''
for i in range(0, 5):
    j = 0
    k = 0
    while j < len(a):
        print("a value is here")
        print(a)
        print(type(a))
        print("j value is here")
        print(j)
        print("k value is here")
        print(k)

        while k < len(a) and a[k] == a[j]: k += 1
        b += str(k-j) + a[j]
        j = k
    print(b)
    print()
    a = b
    b = ''
    
print(len(a))