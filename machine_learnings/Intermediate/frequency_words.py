#Count the frequency of words in a sentence.
String=str(input("Enter any sentance: "))
String=String.lower()
String=String.split()
dic={}
for i in String:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
print(dic)
