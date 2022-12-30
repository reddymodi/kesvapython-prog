def toggle(s1,s2):
    l1=len(s1)
    l2=len(s2)
    if l1 == l2:
        for i in s1:
            if i not in s2:
                print("not a angram")
            else:
                print("its anagram")
    else:
        print("its not a anagram strings")

s1=input()
s2=input()
toggle()
    