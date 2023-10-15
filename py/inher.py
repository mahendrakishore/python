
class P():
    def __init__(self,x):
        print(x)

class C(P):
    def __init__(self,x):
        super().__init__(x)


x = [1,2,3]
c = C(x)