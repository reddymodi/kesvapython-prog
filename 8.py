n=int(input())
k=n
v=0
while n>=0:
    r = k%10
    v = v * 10 + r
    k = k//10
if n == v:
    print("its palindrome")
else:
    print("its not apalindrome")