s={}
def dic(n):
    for i in n:
        k=""
        for j in i:
            j=chr(ord(j)-32)
            k += j 
        l=len(k)
        s[k]=l
n=input().split()
dic(n)
print(s)