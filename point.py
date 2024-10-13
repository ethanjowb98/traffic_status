class Point:
    def __init__(self, x_input: float, y_input: float):
        if not (isinstance(x_input, float) or isinstance(x_input, int)):
            raise Exception
        if not (isinstance(y_input, float) or isinstance(y_input, int)):
            raise Exception
        self.x = x_input
        self.y = y_input

    def __str__(self):
        return "{" + f"{self.x}" + ", " + f"{self.y}" + "}"
        
def point_slope_function(point_a: Point, point_b: Point) -> float:
    return (point_a.y - point_b.y) / (point_a.x - point_b.x)
    
def input_point() -> Point:
    x = float(input("Please input x: "))
    y = float(input("Please input y: "))
    return Point(x, y)
    
while True:
    print("Input point a:")
    a = input_point()
    print("Input point b:")
    b = input_point()
    
    print(f"The slope of point a ({a}) and point b ({b}) is {point_slope_function(a,b)}")
    
    if str(input("Do you want to calculate again? [Y/N]")) == "N":
        break