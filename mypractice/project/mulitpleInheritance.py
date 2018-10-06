class A(object):
    def whereami(slef):
        print("i am in  A")

class B():
    def whereami(slef):
        print("i am in  B")

class C(B,A):
##    def whereami(slef):
##        print("i am in C")
    pass

class D(C,B):
##    def whereami(slef):
##        print("i am in  A")
    pass
    
d = D()
print(D.mro())
#print(D.id)
#print(d.__mro__)
#print(dir(d))
d.whereami()
#d.whoami()


##class A:
##    def__print():
##        print("print A")
##
##class A:
##    def__print():
##        print("print A")
##
##class A:
##    def__print():
##        print("print A")
##
##class A:
##    def__print():
##        print("print A")

        
