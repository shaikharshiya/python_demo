def add():
    print("Addition",a+b)
def sub():
    print("Substraction",a-b)
def mul():
    print("Multiplication",a*b)
def div():
    print("Division",a/b)
while(1):
    print("1.Addition 2.Substraction 3.Multiplication 4.Division 5.Exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        print("Enter 2 numbers :")
        a = int(input("enter 1 no :"))
        b = int(input("enter 2 no :"))
        add()
    elif choice==2:
        print("Enter 2 numbers :")
        a = int(input("enter 1 no :"))
        b = int(input("enter 2 no :"))
        sub()
    elif choice==3:
        print("Enter 2 numbers :")
        a = int(input("enter 1 no :"))
        b = int(input("enter 2 no :"))
        mul()
    elif choice==4:
        print("Enter 2 numbers :")
        a = int(input("enter 1 no :"))
        b = int(input("enter 2 no :"))
        div()
    elif choice==5:
        exit()
    else:
        print("Wrong choice")