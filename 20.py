def cap(n):
    l = len(n)
    i = 0

    while i<l-1:
        count=1
        while(i<l-1and (n[i]==n[i+1])):
            count += 1 
            i += 1
        i += 1 
        print(n[i-1]+str(count),end="")
n = input("enter the charecters: ")
cap(n)
