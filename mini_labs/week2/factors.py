
def factors(n):
    factors = []
    x = range(1, n + 1)
    for i in x:
        if (n % i == 0):
            factors.append(i)
            print(i, end=' ')
          
    print(factors)


class Factors:
    def __init__(self):
        self.factors = []
      
    def __call__(self, n):
      for i in range(1, n + 1):
        if n % i == 0:
            self.factors.append(i)
      return self.factors
      
factors_of = Factors() # object instantiation and run __init__ method
print(factors_of(0)) # object running __call__ method



def tester():
  factors(89)
  factors(66)
  try:
    n = int(input("Pick a Number to Get the Factors of"))
    if not (isinstance(n, int) and n >= 0):
      raise ValueError
    print("Factors of {0} is: ".format(n))
    print(factors_of(n)) # print the nth term
  except:
    print(f'Positive integer number expected, got "{n}" Try again.')

if __name__ == "__main__":
    tester()