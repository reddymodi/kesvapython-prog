
l = []
def loop(n):
    if n == 0:
        return 1
    else:
        k = n%10
        l.append(k)
        loop(n//10)
        
n=int(input("enter a charecter: "))
loop(n)
print(sum(l))