#Count vowels and consonants in a string
String=str(input("Enter a string: "))
dic={'A':'a','E':'e','I':'i','O': 'o','U':'u','u':'U','o' :'O','i':'I','e':'E','a':'A'}
count=0
for i in range(len(String)):
    if String[i] in dic:
        count+=1
print(count)