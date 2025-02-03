class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("The denominator cannot be 0.")

        if isinstance(numerator,float) or isinstance(denominator,float):
            self.numerator = 0
            self.denominator = 1
        
        if isinstance(numerator,str) and denominator == 1:
            fraction_string = numerator.strip()

            if '/' in fraction_string:
                if fraction_string.count('/') > 1:
                    self.numerator = 0
                    self.denominator = 1
                
                else:
                    try:
                        fraction_string = fraction_string.split('/')
                        num, denom = int(fraction_string[0]), int(fraction_string[1])

                        if denom == 0:
                            raise ZeroDivisionError("The denominator cannot be 0.")
                            
                        self.numerator, self.denominator = num, denom
                    
                    except ValueError:
                        self.numerator = 0
                        self.denominator = 1
            
            elif "." in fraction_string:
                self.numerator = 0
                self.denominator = 1

            
            elif any(c.isalpha() for c in fraction_string):
                self.numerator = 0
                self.denominator = 1

            else: 
                self.numerator = numerator
                self.denominator = denominator

        elif isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator
            
        else:
            self.numerator = 0
            self.denominator = 1
            
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
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def get_fraction(self):
        numerator = self.get_numerator()
        denominator = self.get_denominator()
        gcd = Fraction.gcd(self.numerator, self.denominator)

        if numerator == 0:
            return "0"
        
        if denominator == 1:
            return numerator
        
        if gcd != 0:
            numerator = numerator //gcd
            denominator = denominator //gcd 

        if denominator < 0:
            numerator = numerator*-1
            denominator = denominator*-1

        return str(numerator) + "/" + str(denominator)

        
        
        

