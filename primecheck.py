num=int(input("enter a number:"))
count=0
for i in range(1,num):
    if num%i==0:
        count+=1
if count>2:
    print("not a prime number")
else:
    print("prime number")
    
