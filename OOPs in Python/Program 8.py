import math

def area(a=None, b=None, c=None):
    
    # Square
    if a is not None and b is None and c is None:
        print("Area of Square:", a * a)

    # Rectangle
    elif a is not None and b is not None and c is None:
        print("Area of Rectangle:", a * b)

    # Triangle
    elif a is not None and b is not None and c is not None:
        print("Area of Triangle:", (a * b) / 2)

    # Circle
    elif a is not None and b is None:
        print("Area of Circle:", math.pi * a * a)

    # Ellipse
    elif a is not None and b is not None:
        print("Area of Ellipse:", math.pi * a * b)


area(4)          # Square
area(5, 6)       # Rectangle
area(6, 8, 1)    # Triangle
print("Area of Circle:", math.pi * 3 * 3)
print("Area of Ellipse:", math.pi * 4 * 5)