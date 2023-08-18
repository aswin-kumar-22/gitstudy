num=int(input("Enter a range of limit :"))
list1=[]
for i in range(2,num): 
    for j in range(2,num):
        if i%j == 0:
            break
    if i == j:
        list1.append(i)
pal=[]
for i in list1:
    temp=i
    rev=0
    while(i>0):
        dig=i%10
        rev=rev*10+dig
        i=i//10
    if (temp==rev):
        pal.append(temp)
print(max(pal))