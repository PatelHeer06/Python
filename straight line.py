#straight line
a=int(input("Enter x1:"))
b=int(input("Enter x2:"))
c=int(input("Enter x3:"))
d=int(input("Enter y1:"))
e=int(input("Enter y2:"))
f=int(input("Enter y3:"))
m1=(b-a)/(e-d)
m2=(c-a)/(f-d)
if(m1==m2):
    print("Straight line")
else:
    print("not straight line")
