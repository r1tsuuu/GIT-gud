class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator,float) or isinstance(denominator,float):
            print("Invalid input") 
            return
        
        if isinstance(numerator,str):
            for char in numerator:
                if char.isdigit():
                 result = numerator.split("/")
                 self.numerator = int(result[0])
                 self.denominator = int(result[1])
                 break

        
        if denominator == 0:
            raise ZeroDivisionError
        
        
        if isinstance(numerator,int) and isinstance(denominator,int):
            self.numerator = int(numerator)
            self.denominator = int(denominator)

    def gcd(a, b):
        """
        Return the Greatest Common Divisor (GCD) of two integers.
        If one or both of them is 0, then it returns 0.
        """
        if a == 0 or b == 0:
            return 0

        while b:
            a, b = b, a % b  # Apply Euclidean algorithm

        return abs(a)  # Ensure non-negative output

    def get_numerator(self):
        return str(self.numerator)

    def get_denominator(self):
        return str(self.denominator)

    def get_fraction(self):
        #TODO Attribute error need to debug
        if self.denominator == 1:
            return self.numerator
        
        if self.numerator % self.denominator == 0:
            return self.numerator // self.denominator
        else :
            return str(self.numerator) + "/" + str(self.denominator)
        


