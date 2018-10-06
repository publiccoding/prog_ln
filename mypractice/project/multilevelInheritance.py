class A:
    def __init__(self):
        print("i am in A")
class B(A):
##    def __init__(self):
##        print("i am in B")
    pass
class C(B):
##    def __init__(self):
##        print("i am in C")
    pass 
c = C()


                            
