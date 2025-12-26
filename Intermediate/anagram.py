#Check if two strings are anagrams (e.g., "listen" and "silent").
s1=str(input("Enter any string: "))
s2=str(input("Enter any string: "))
s1=s1.replace(' ','').lower()
s2=s2.replace(' ','').lower()
if len(s1) != len(s2):
    print('not an anagram')
else:
    s2_list=list(s2)
    is_anagram=True
    for i in s1:
        if i in s2_list:
            s2_list.remove(i)
        else:
            is_anagram=False
            break
if is_anagram==True:
    print("anagram")
else:
    print("not an anagram")