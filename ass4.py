l=[]
a=int(input("Enter How many numbers you want to Enter="))
for i in range(a):
    b=int(input())
    l.append(b)

for i in l:
    if i % 2== 0:
        print(i, " is even ")
    elif i%2!=0:
        print(i," is odd")

