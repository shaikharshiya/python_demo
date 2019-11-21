l=[]
a=int(input("Enter How many numbers you want to Enter="))
for i in range(a):
    b=int(input())
    l.append(b)
c=len(l)
for i in l:
    if i % 2== 0:
        print(i, " is even ")
    elif i%2!=0:
        print(i," is odd")

    elif i%i==0:
        print(i,"is prime")
        

    
l.sort()
print("Smallest Number =",l[0])
print("Largest Number = ",l[c-1])

