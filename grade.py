a=float(input("Enter marks of maths:"))
b=float(input("Enter marks of physics:"))
c=float(input("Enter marks of chemistry:"))
d=a+b+c
e=d/3
print("Total:",d)
print("Average:",e)
if(0<d<39):
    print("F")
elif(40<d<44):
    print("P")
elif(45<d<49):
    print("C")
elif(50<d<54):
    print("B")
elif(55<d<59):
    print("B+")
elif(60<d<69):
    print("A")
elif(70<d<79):
    print("A+")
elif(80<d<100):
    print("O")
