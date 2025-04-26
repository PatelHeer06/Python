def circle():
    x=float(input("x= :"))
    y=float(input("y= :"))
    r=float(input("radius= :"))
    x1=float(input("x1= :"))
    y1=float(input("y1= :"))
    if (pow((x1-x),2)+pow((y1-y),2))==pow(r,2) :
        print("On the circle")
    
    if (pow((x1-x),2)+pow((y1-y),2))>pow(r,2) :
        print("Outside the circle")
    
    if (pow((x1-x),2)+pow((y1-y),2))<pow(r,2) :
        print("Inside the circle")
circle()
circle()
circle()
