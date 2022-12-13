num=int(input("enter a number:"))
num1=num
rev=0
while num!=0:
    n=num%10
    rev=rev*10+n
    num//=10
if num1==rev:
    print("palindrome")
else:
    print("not a palidrome")
