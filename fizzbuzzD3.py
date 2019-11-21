number=int(input("Enter number"))
for fizzbuzz in range(1,number+1):
    if fizzbuzz % 3==0 and fizzbuzz%5==0:
        print("Fizz-Buzz")
    elif fizzbuzz % 3==0:
        print("Fizz")
    elif fizzbuzz % 5==0:
        print("Buzz")
    else:
        print(fizzbuzz)
