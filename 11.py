n=input()
s = " "
for i in range(len(n)):
    if n[i] == " ":
        s += n[i]
    else:
        if i % 2 != 0:
            if "a"<=n[i]<="z":
                c = ord(n[i])
                c = c-32
                ch = chr(c)
                s += ch 
            else:
                k = ord(n[i])
                c = k + 32
                ch = chr(c)
                s += ch 
        else:
            s += n[i]
                
print(s)