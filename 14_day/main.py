class vector:
    def __init__(self,component):
        self.component = component
        self.n = len(component)
    def __add__(self,other):
        if self.n != other.n:
            raise ValueError("vector must be same dimention for addition")
        sum = [self.component[i]+other.component[i] for i in range(self.n)]
        return vector(sum)
    def __mul__(self,other):
        if self.n != other.n:
            raise ValueError("vector must be in same dimention for multiply")
        reasult = [self.component[i]*other.component[i] for i in range(self.n)]
        return vector(reasult)
    def __str__(self):
        return (f"vector{self.component}")
    def __len__(self):
        return self.n
v1 = vector([3,5,7])
v2 = vector([5,7,78])
v = v1+v2
print(v)