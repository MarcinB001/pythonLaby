class Complex:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex( self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex( self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


a = Complex(1,-3)
b = Complex(2,-6)

print(a+b)
print(a-b)