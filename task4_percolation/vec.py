from numbers import Number

class _v2:
    def __init__(self, x: Number, y: Number):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'({self.x}, {self.y})'
    def __str__(self):
        return self.__repr__()
    def __add__(self, other):
        return v2(self.x + other.x, self.y + other.y)
    def __radd__(self, other):
        return self + other
    def __mul__(self, other: Number):
        return v2(self.x * other, self.y * other)
    def __rmul__(self, other: Number):
        return self * other
    def __neg__(self):
        return self * (-1)
    def __sub__(self, other):
        return self + (-other)
    def __rsub__(self, other):
        return (-self) + other
    def __iter__(self):
        yield self.x
        yield self.y

class _v3(_v2):
    def __init__(self, x: Number, y: Number, z: Number):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'
    def __str__(self):
        return self.__repr__()
    def __add__(self, other):
        return _v3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __mul__(self, other: Number):
        return _v3(self.x * other, self.y * other, self.z * other)
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

class v2(_v2):
    ex = _v2(1,0)
    ey = _v2(0,1)
class v3(_v3):
    ex = _v3(1, 0, 0)
    ey = _v3(0, 1, 0)
    ez = _v3(0, 0, 1)