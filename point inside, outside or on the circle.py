a=int(input("Enter radius:"))
b=int(input("X1:"))
c=int(input("X2:"))
d=int(input("Y1:"))
e=int(input("Y2:"))
f=a**2
g=(c-b)**2
h=(e-d)**2
if(f==(g+h)):
    print("Point is on the circle")
elif(f<(g+h)):
    print("Point is outside the circle")
else:
    print("Point is inside the circle")
