def prime(n):
    a=0
    b=int(pow(n,0.5))
    for i in range(2,b+1) :
        if n%i==0 :
            a=1
    if a==0 :
        print("Prime")

def perfect(n):
    sum=0
    c=n//2
    for i in range(1,c+1) :
        if n%i==0 :
            sum=sum+i
    if sum==n :
        print("Perfect")

def armstrong(n):
    check=n
    rem=0
    sum=0
    while n>0 :
        rem=n%10
        n=n//10
        sum=sum + rem*rem*rem
    if sum==check :
        print("Armstrong")

def palindrome(n):
    rev=0
    ld=0
    check=n
    while n>0:
        ld=n%10
        rev=rev*10 + ld
        n=n//10
    if rev==check:
        print("Palindrome")

def automorphic(n):
    d=n**2
    count=0
    check=n
    
    while check>0 :
        check=check//10
        count=count+1
    s=10**count
    g=d%s
    if n==g :
        print("Automorphic")
        
n=int(input("Enter a number : "))


prime(n)
perfect(n)
armstrong(n)
palindrome(n)
automorphic(n)
