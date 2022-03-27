n = int(input("Pick a Number to Get the Factors of"))


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
print(factors_of(5)) # object running __call__ method



def tester():
  factors(89)
  factors(66)
  print(factors_of(88))

if __name__ == "__main__":
    tester()