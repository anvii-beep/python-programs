def check_right_triangle(a, b, c):
    if a**2 + b**2 == c**2:
        print("It is a right-angled triangle")
    else:
        print("It is not a right-angled triangle")


a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

check_right_triangle(a, b, c)
