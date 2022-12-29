n=int(input())
a = 0
b = 1
c = 1
if (n==0 or n==1):
    ("its a fbonacci number")
else:
    while a < n:
        a = b+c
        c = b 
        b = a 
    if a == n:
        print("it s fabonacci")
    else:
        print("its not a fabonacci")
        