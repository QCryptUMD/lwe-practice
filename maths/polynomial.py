from dataclasses import dataclass

# note: specialized for Z_2[x]/(x^256 + 1)
MOD = 2
DEGREE = 256
PMOD = [1] + [0]*255 + [1] # unused

@dataclass(frozen=True)
class Polynomial():
    coefficients : tuple[int]
    
    @classmethod
    def from_coefficients(cls, coefficients):
        return cls.reduce(cls(coefficients=tuple(coefficients)))
    
    @classmethod
    def reduce(cls, poly):
        coefficients = [0] * DEGREE
        
        # this only works for x^DEGREE + 1
        for i in range(1 + len(poly.coefficients) // DEGREE):
            slice = poly.coefficients[i*DEGREE:(i+1)*DEGREE]
            for i, c in enumerate(slice):
                coefficients[i] -= c
        
        # reduce the coefficients
        for i in range(len(coefficients)):
            coefficients[i] %= MOD
            
        return cls(coefficients=coefficients)
    
    @classmethod
    def add(cls, p1, p2):
        return cls.from_coefficients([a + b for a, b in zip(p1.coefficients, p2.coefficients)])
    
    @classmethod
    def multiply(cls, p1, p2):
        p1 = cls.reduce(p1)
        p2 = cls.reduce(p2)
        
        coefficients = [0] * DEGREE * 2
        for i, c1 in enumerate(p1.coefficients):
            for j, c2 in enumerate(p2.coefficients):
                coefficients[i+j] += c1 * c2
        return cls.from_coefficients(coefficients)
        
    def __add__(self, other):
        return self.add(self, other)
    
    def __mul__(self, other):
        return self.multiply(self, other)
    
    def __repr__(self):
        return '<' + ' + '.join([f'{c}x^{i}' for i, c in enumerate(self.coefficients) if c != 0]) + '>'
    

# tests
if __name__ == '__main__':
    c1 = Polynomial.from_coefficients([0,1,0,1])
    c2 = Polynomial.from_coefficients([1,1,0,0,0,0,0,0,0,0,0,1])
    c3 = Polynomial.from_coefficients([0, 1, 0, 0, 1, 1])
    
    print(c1)
    print(c2)
    print(c3)
    print('--')
    print(c1 + c2)
    print(c1 * c2)