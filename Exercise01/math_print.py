import math

def golden_ratio():
    print((1+math.sqrt(5))/2)

def six_squared():
    print(math.pow(6,2))

def hypotenuse():
    print(math.sqrt((math.pow(5,2) + math.pow(12,2))))

def pi():
    print(math.pi)

def e():
    print(math.e)

def squares_area():
    print(math.pow(1,2), math.pow(2,2),math.pow(3,2),math.pow(4,2),math.pow(5,2),math.pow(6,2),math.pow(7,2),math.pow(8,2),math.pow(9,2),math.pow(10,2))


if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()