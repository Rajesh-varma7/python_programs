def factorial(p_num):
  factorial = 1
  if p_num < 0:
    retun 'Factorial does not exist for negative numbers'
  elif p_num == 0:
    return 'The factorial of 0 is 1'
  else:
    for i in range(1,p_num + 1):
      factorail = factorial * i
    return f"The factorial of {p_num} is {factorial}"
print(factorial(10))
