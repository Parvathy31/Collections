str1=input("Enter the string")
length=len(str1)
if length>2:
    if str1[-3:]=='ing':
     str1+='ly'
    else:
        str1+='ing'
    print("New String:",str1)
        
