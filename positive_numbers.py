i=1
lst2=[]
while True:
    if i > 1:
        n=input("Do you want to enter another list?(Y/N)")
        if n=="N":
            break
    lst=eval(input("Enter list{} = ".format(i)))
    for item in lst:
        if float(item)>0:
            lst2.append(item)
    print(lst2)
    print()
    i+=1
    lst2=[]
