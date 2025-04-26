def areaorper():
    a=float(input("Enter Length : "))
    b=float(input("Enter Breadth : "))
    area=a*b
    perimeter=2*(a+b)
    if area>perimeter :
        print("Area is greater")
    if perimeter>area :
        print("Perimeter is greater")
    if perimeter==area :
        print("Both are equal")
        
areaorper()
