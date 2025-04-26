def SLof3():
    a=float(input("Enter a number : "))
    b=float(input("Enter second number : "))
    c=float(input("Enter third number : "))
    if a>b and a>c :
        print(a," is largest")
    if b>a and b>c :
        print(b," is largest")
    if c>a and c>b :
        print(c," is largest")
    if a<b and a<c :
        print(a," is smallest")
    if b<a and b<c :
        print(b," is smallest")
    if c<b and c<a :
        print(c," is smallest")
SLof3()
        
