def result():
    a=float(input("Enter marks of subject 1 : "))
    b=float(input("Enter marks of subject 2 : "))
    c=float(input("Enter marks of subject 3 : "))
    avg=(a+b+c)/3
    total=a+b+c
    print("Average = ",avg)
    print("Total = ",total)
    print("In subject 1 : ")
    if 80<=a<=100 :
        print("O grade")
    
    elif 70<=a<=79 :
        print("A+ grade")
    
    elif 60<=a<=69 :
        print("A grade")
    
    elif 55<=a<=59 :
        print("B+ grade")
    
    elif 50<=a<=54 :
        print("B grade")
        
    elif 45<=a<=49 :
        print("C grade")
    
    elif 40<=a<=44 :
        print("P grade")
    
    elif b<=39 :
        print("Fail")
    else :
        print("")
    print("In subject 2 : ")    
        
    if 80<=b<=100 :
         
         print("O grade")
    
    elif 70<=b<=79 :
         print("A+ grade")
    
    elif 60<=b<=69 :
         print("A grade")
    
    elif 55<=b<=59 :
         print("B+ grade")
    
    elif 50<=b<=54 :
         print("B grade")
    
    elif 45<=b<=49 :
         print("C grade")
    
    elif 40<=b<=44 :
         print("P grade")
    
    elif b<=39 :
         print("Fail")
    else :
         print("")
    print("In subject 3 : ")
     
    if 80<=c<=100 :
         print("O grade")
    
    elif 70<=c<=79 :
         print("A+ grade")
    
    elif 60<=c<=69 :
         print("A grade")
    
    elif 55<=c<=59 :
         print("B+ grade")
    
    elif 50<=c<=54 :
         print("B grade")
        
    elif 45<=c<=49 :
         print("C grade")
    
    elif 40<=c<=44 :
         print("P grade")
    
    elif c<=39 :
         print("Fail")
    else :
         print("")

result()
    
    
