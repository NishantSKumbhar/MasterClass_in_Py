import sys

class ProductDimension:
    def __init__(self, length: float, breadth: float, depth: float):
        self.L = length
        self.B = breadth
        self.H = depth


class TV:
    def __init__(self, tv_brand_name: str, tv_screen_resolution: tuple, tv_dimensions: ProductDimension,
                 tv_technology: str):
        if (type(tv_brand_name) != str or
                type(tv_screen_resolution) != tuple or
                type(tv_dimensions) != ProductDimension or
                type(tv_technology) != str):
            print("Error")
            sys.exit(-1)
        self.tv_brand_name = tv_brand_name
        self.tv_screen_resolution = tv_screen_resolution
        self.tv_dimensions = tv_dimensions
        self.tv_technology = tv_technology

    def compare(self, other):   # def compare(self : TV, t2 : TV):
        if self.tv_screen_resolution == other.tv_screen_resolution:
            print("Yes")
        else:
            print("No")
        if type(other) != TV and type(self) != TV:
            print("error")
        else:
            print("no error")



mytv1 = TV("LG", (1920, 1080), ProductDimension(70, 45, 5), "OLED")
mytv2= TV("SONY", (1920, 1080), ProductDimension(45, 20 , 5), "LED")
mytv1.compare(mytv2)            # or  TV.compare(mytv1, mytv2)
