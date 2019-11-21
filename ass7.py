
stu_list=[(1,6223100,'10/12/2018'), (2,6223101,'11/1/2019'), (3,6223102,'2/2/2019'), (4,6223103,'5/3/2019'), (5,6223104,'8/6/2019')]


choice=1
while choice!=0:
    print()
    
    print("1. Search by book number")
    print("2. Search by student id")
    print("3. Search by date")
    print("0. Exit")
    choice=int(input("Enter choice: "))
    if choice==1:
        a=int(input("Enter Bookno  :"))
        l=len(stu_list)
        for i in range(l):
            if a==stu_list[i][1]:
                print("",stu_list[i][1:])
    elif choice==2:
        a=int(input("Enter Id :"))
        l=len(stu_list)
        for i in range(l):
            if a==stu_list[i][0]:
                print(stu_list[i][:2])
    elif choice==3:
        print(stu_list) 
        a=str(input("Enter Date :"))
        l=len(stu_list)
       
        for i in range(l):
            
            if a==stu_list[i][2]:
                print(stu_list[i][:2])
    elif choice==0:
        print("Exiting!!!")
    else:
        print("Invalid choice!!")
print()
