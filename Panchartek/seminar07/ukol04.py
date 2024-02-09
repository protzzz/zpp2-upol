def factorial_konc(n, result=1):
   try:
      assert n > 0
   except AssertionError:
     return "factorial zapornych cisel neexistuje"

   if n == 0:
      return result
   else:
      return factorial_konc(n-1, result*n)

print(factorial_konc(-1))