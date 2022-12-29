n = input()
s=" "
for i in n:
    if i == " ":
        s += i 
    else:
        i = ord(i) + 1
        c = chr(i)
        s += c 
k = s.split()
print(k)
print(s)
    