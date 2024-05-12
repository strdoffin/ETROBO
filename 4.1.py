import math
def calCylider(r,h):
    return math.pi * (r**2) * h
def calCone(r,h):
    return (1/3) * h * math.pi * (r**2)
def calShphere(r):
    return (4/3) * math.pi * (r**3)


def main() :
    r = float(input("Enter radius:"))
    h = float(input("Enter height:"))
    print("Cylinder volume:",calCylider(r,h))
    print("Cone volume:",calCone(r,h))
    print("Sphere volume: ",calShphere(r))

main()