r=[]
areas=[]
a=int(input("Enter How many Radius You want to enter :"))
pi=3.14
print("Enter ",a," Radius Values =")
for i in range(a):
    b=float(input())
    r.append(b)
    
print("Radius Values =",r)

for i in r:
    area=pi*i*i
    areas.append(area)

print("Area of Circle =",areas)
