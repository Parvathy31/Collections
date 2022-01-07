n=int(input("Enter the number"))
def add(n):
    while n>0:
        s=0
        d=n%10
        s=s+d
        n=n/10
    print("The sum of digits of number is : ",s)
    return s
add(n)
