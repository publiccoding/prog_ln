##class shark():
##    def swim(self):
##        print("The shark is swiming")
##    def swim_backwards(self):
##        print("The share cannot swim backward, but it can shink backwared")
##    def skeleton(self):
##        print("The shark's is made of caritagle")
##
##class clownfish():
##    def swim(self):
##        print("The clownfish is swiming")
##    def swim_backwards(self):
##        print("The clownfish cannot swim backward, but it can shink backwared")
##    def skeleton(self):
##        print("The clownfish's is made of caritagle")
##
##
##def duck_typing(fish):
##    fish.swim()
##    fish.swim_backwards()
##    fish.skeleton()
##
##
##shark = shark()
##clownfish = clownfish()
##
##
##duck_typing(shark)
##duck_typing(clownfish)

    



## polymorphism with abstract class

class Document:
    def __init__(self,name):
        self.name=name
    def show(self):
        raise NotImplementedError("subclass must implement abstract method")
class Pdf(Document):
    def Short(self):
        return "show pdf contents!"

class Word(Document):
    def show(self):
        return "show word contents!"

documents = [Pdf('Document1'),Pdf('Document2'),Word('Document3')]

for doc in documents:
    print(doc.name + ':' + doc.show())

































    
