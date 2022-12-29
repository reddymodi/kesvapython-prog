def pen(n):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    k = ""
    for i in n:
        if i == " ":
            k += i 
        elif i in vowels:
            m = ord(i)+1
            ch = chr(m)
            k += ch 
        else:
            k += i 
    return k 

n=input()
print(pen(n))            