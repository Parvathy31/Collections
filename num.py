num1=input("Enter the integer list(space separated):")
num=list(map(int,num1.split()))
num=[x for x in num if x%2!=0]
print("List after removing even numbers",end='')
print(num)
