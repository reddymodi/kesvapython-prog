n=list(map(int,(input().split(" "))))
temp = n[0]
for i in range(1,len(n)):
    if n[i] > temp:
        temp=n[i]
print(temp)