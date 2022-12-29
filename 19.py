def loop(n):
    if len(n) == 0:
        return n
    else:
        return loop(n[1:])+n[0]
n=input("enter a charecter: ")
print(loop(n))