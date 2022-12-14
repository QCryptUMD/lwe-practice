from dataclasses import dataclass
from typing import Iterable
from typing_extensions import Self

MOD = 3329
DEGREE = 256

@dataclass(frozen=True)
class Polynomial():
    coefficients : tuple[int, ...]

    @classmethod
    def from_coefficients(cls, coefficients: Iterable[int]) -> Self:
        return cls.reduce(cls(coefficients=tuple(coefficients)))

    @classmethod
    def reduce(cls, poly: Self) -> Self:
        coefficients = [0] * DEGREE

        # this only works for x^DEGREE + 1
        for i in range(1 + len(poly.coefficients) // DEGREE):
            slice = poly.coefficients[i*DEGREE:(i+1)*DEGREE]
            for j, c in enumerate(slice):
                coefficients[j] += c * (-1) ** i

        # reduce the coefficients
        for i in range(len(coefficients)):
            coefficients[i] %= MOD

        return cls(coefficients=coefficients)

    def __neg__(self) -> Self:
        coeffs = [-c for c in self.coefficients]
        return self.from_coefficients(coeffs)
    
    def __add__(self, other: Self) -> Self:
        p1 = self.reduce(self)
        p2 = self.reduce(other)
        
        coefficients = [0] * DEGREE

        for i in range(DEGREE):
            if i < len(p1.coefficients):
                coefficients[i] += p1.coefficients[i]
            if i < len(p2.coefficients):
                coefficients[i] += p2.coefficients[i]

        return self.from_coefficients(coefficients)

    def __mul__(self, other: Self) -> Self:
        p1 = self.reduce(self)
        p2 = self.reduce(other)

        coefficients = [0] * DEGREE * 2
        for i, c1 in enumerate(p1.coefficients):
            for j, c2 in enumerate(p2.coefficients):
                coefficients[i + j] += c1 * c2
        return self.from_coefficients(coefficients)
    
    def __sub__(self, other: Self) -> Self:
        return self + -other

    def __rsub__(self, other: Self) -> Self:
        return other + -self

    def __repr__(self) -> str:
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
    print(-c2)
    print(c1 - c2)
    print(c1 * c2)
