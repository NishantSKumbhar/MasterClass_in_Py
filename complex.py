class Complex:

    def __init__(self, x: float, y: float):
        """
        Constructor of Complex Class
        :param x:  real part
        :param y:  imaginary part
        """
        self.re = x
        self.im = y


c1 = Complex(1.1, 2.2)
c2 = Complex(8.3, 2.1)
print(c1.__dict__)
print(c2.__dict__)