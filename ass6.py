l=[]
l1=[]
l2=[]
a=int(input("Enter How many numbers you want to Enter="))
print("Enter ",a,"values :")
for i in range(a):
    b=int(input())
    l.append(b)
c=len(l)
m=int(input("Enter Median number :"))
for i in l:
    if m in l :
        l.remove(m)

    if i<m:
        l1.append(i)
    else:
        l2.append(i)

print("L1 =" ,l1)
print("L2 =", l2)

