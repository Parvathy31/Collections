list=input("Enter the list")
list1=map(int,list.split())
sum=0
for i in list1:sum+=i
print("The sum of all iterms in list",list,"is",sum)
