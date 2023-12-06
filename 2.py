import math


def read():
    x = int(input("Enter first side of first triangle: "))
    y = int(input("Enter second side of first triangle: "))
    z = int(input("Enter third side of first triangle: "))
    a = int(input("Enter first side of second triangle: "))
    b = int(input("Enter second side of second triangle: "))
    c = int(input("Enter third side of second traingle: "))
    return x, y, z, a, b, c


def area(x,y,z,a,b,c):
    s1 = (x+y+z)/2

    area1 = math.sqrt(s1*(s1-x)*(s1-y)*(s1-z))

    s2 = (a+b+c)/2
    area2 = math.sqrt(s2*(s2-a)*(s2-b)*(s2-c))

    return area1,area2

def total(area1, area2):
    total = area1 + area2
    return total


def contribution(area1,area2,total):
    c1 = (area1/total)*100
    c2 = (area2/total)*100

    return c1,c2

x, y, z, a, b, c = read()

area1, area2 = area(x, y, z, a, b, c)

total_area = total(area1, area2)

c1, c2 = contribution(area1, area2, total_area)


print(f"Area of first triangle: {area1}")
print(f"Area of second triangle: {area2}")
print(f"Total area: {total_area}")
print(f"Contribution of first triangle: {c1}%")
print(f"Contribution of second triangle: {c2}%")