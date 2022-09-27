import random
coefficients = []
for i in range(768):
  sum = 0
  for i in range(6):
    if i > 2:
      sum -= random.randrange(0,2)
    else:
      sum += random.randrange(0,2)
  coefficients.append(sum)
error_components = [Polynomial.from_coefficients(coefficients[:256]), 
                    Polynomial.from_coefficients(coefficients[256:512]), 
                    Polynomial.from_coefficients(coefficients[512:])]