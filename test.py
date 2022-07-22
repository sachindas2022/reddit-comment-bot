num = int(input("enter a number"))

n = num

while n > 10:

    n = n // 10
    if n==0:
        print("{} is the first digit of {}".format(n,num))
    else:
        print("{} is the first digit of {}".format(n, num))