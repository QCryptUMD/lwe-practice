from maths.polynomial import Polynomial
import random

class ErrorGenerator():
    @staticmethod
    def generate():
      coefficients = []

      for i in range(768):
        sum = 0
        for j in range(6):
          if j > 2:
            sum -= random.randrange(0,2)
          else:
            sum += random.randrange(0,2)
        coefficients.append(sum)

      return [Polynomial.from_coefficients(coefficients[:256]),
              Polynomial.from_coefficients(coefficients[256:512]),
              Polynomial.from_coefficients(coefficients[512:])]


