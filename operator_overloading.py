class book:
    def __init__(self, n, p):
        self.bookname = n
        self.price = p
    def __add__(self,other):
        return self.price + other.price
    def __mul__(self,other):
        return self.price * other.price
    def __truediv__(self,other):
        return self.price / other.price
    def __sub__(self,other):
        return self.price - other.price
    def __floordiv__(self,other):
        return self.price // other.price
    def __mod__(self,other):
        return self.price % other.price
    def __pow__(self,other):
        return self.price ** other.price
    def __eq__(self,other):
        return self.price == other.price
    def __ne__(self,other):
        return self.price != other.price
    def __lt__(self,other):
        return self.price < other.price
    def __le__(self,other):
        return self.price <= other.price
    def __gt__(self,other):
        return self.price > other.price
    def __ge__(self,other):
        return self.price >= other.price
    def __iadd__(self, other):
        print("__iadd__")
        self.price += other.price
        return self
    def __isub__(self, other):
        print("__isub__")
        self.price -= other.price
        return self
    def __imul__(self, other):
        print("__imul__")
        self.price *= other.price
        return self
    def __itruediv__(self, other):
        print("__itruediv__")
        self.price /= other.price
        return self
    def __ifloordiv__(self, other):
        print("__ifloordiv__")
        self.price //= other.price
        return self
    def __imod__(self, other):
        print("__imod__")
        self.price %= other.price
        return self
    def __ipow__(self, other):
        print("__ipow__")
        self.price **= other.price
        return self
    def __and__(self, other):
        print("__and__")
        return int(self.price) & int(other.price)
    def __or__(self, other):
        print("__or__")
        return int(self.price) | int(other.price)
    def __xor__(self, other):
        print("__xor__")
        return int(self.price) ^ int(other.price)
    def __invert__(self):
        print("__invertr__")
        return ~ int(self.price)
    def __lshift__(self, other):
        print("__lshift__")
        return int(self.price) << int(other.price)
    def __rshift__(self, other):
        print("__rshift__")
        return int(self.price) >> int(other.price)
    def display_players(*args):
        print("Displaying all players:")
        for p in args:
            print(p)
b = book("The Secret", 200)
b1 = book("core python",100)
print(b + b1)
print(b * b1)
print(b / b1)
print(b - b1)
print(b // b1)
print(b % b1)
print(b ** b1)   
print(b == b1)
print(b != b1)
print(b < b1)
print(b <= b1)
print(b > b1)
print(b >= b1)
b += b1
print(b.price)
b -= b1
print(b.price)
b *= b1
print(b.price)
b /= b1
print(b.price)
b //= b1
print(b.price)
b %= b1
print(b.price)
b **= b1
print(b.price)
c = book("ABC", 10)
d = book("PQR",2)
print(c & d)
print(c | d)
print(c ^ d)
print(c)
print(c << d)
print(c >> d)

'''
OUTPUT :->
300
20000
2.0
100
2
0
126765060022822940149670320537600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
False
True
False
False
True
True
__iadd__
300
__isub__
200
__imul__
20000
__itruediv__
200.0
__ifloordiv__
2.0
__imod__
2.0
__ipow__
1.2676506002282294e+30
__and__
2
__or__
10
__xor__
8
<__main__.book object at 0x10b37d1d0>
__lshift__
40
__rshift__
2'''