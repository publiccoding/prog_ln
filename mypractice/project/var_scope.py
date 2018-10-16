

global a
a = ' global a'


def outer():

    #global a
    a = ' outer a' # can't declare nonlocal on extreme outer method 

    def inner():

        nonlocal a # you declare nonlocal it will take the inner function scope 
        a = ' inner a'
        print(a)

        def subinner():
            #nonlocal a  # This will have scope on subinner and inner
            global a  # scope gains only after nonlocal 
            a = ' sub inner a'
            print(a)

        subinner()
        print(a)

    inner()
    print(a)


print(a)
outer()
print(a)
