a=int(input("Enter Number ="))
last_no=a % 10
while(a!=0):
    first_no=a%10
    a=a//10
if(first_no==last_no):
    print("Numbers are same")
else:
    print("Numbers are diffrent")
