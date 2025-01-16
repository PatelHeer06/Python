#area greater than perimeter
a=int(input("Enter length:"))
b=int(input("Enter breadth:"))
c=a*b
d=2*(a+b)
if(c>d):
    print("Area is greater")
else:
    print("Perimeter is greater")
