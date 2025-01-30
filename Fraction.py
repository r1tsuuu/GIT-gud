class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if not numerator.isnumeric() and denominator.isnumeric():
            print("Invalid input.")
            return
        
        if denominator == 0:
            print("Cannot divide by 0.")
        
        self.numerator = numerator
        self.denominator = denominator


    def gcd(a, b):
        
        result = min(a, b)

        while result:    
            if (a % result == 0) and (b % result == 0):
                break
            result -= 1
            
        return result

    def get_numerator(self):
        return str(self.numerator)

    def get_denominator(self):
        return str(self.denominator)

    def get_fraction(self):
        if self.denominator == 1:
            return self.numerator
        
        if self.numerator % self.denominator == 0:
            return self.numerator // self.denominator
        else :
            return str(self.numerator) + "/" + str(self.denominator)
        


