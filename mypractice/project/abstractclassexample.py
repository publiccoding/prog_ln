from abc import ABC, abstractmethod


class AbstractExample(ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super(AbstractExample,self).__init__()
        
    @abstractmethod
    def returnValue(self):
        pass
    
class Add(AbstractExample):

    def returnValue(self):
        return self.a + self.b
    
class Mul(AbstractExample):

    def returnValue(self):
        return self.a * self.b

abs1 = Add(4,5)
print(abs1.returnValue())
print(abs1.showing())

abs2 = Mul(5,6)
print(abs2.returnValue())




