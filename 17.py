n=tuple(input().split())
k=()
for i in n:
    if i not in k:
        k.append(i)
print(k)