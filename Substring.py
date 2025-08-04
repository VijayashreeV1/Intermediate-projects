
my_list=["flower","fow","fight"]
p = my_list[0]

for word in my_list[1:]:
    i = 0
    while i < len(p) and i < len(word) and p[i] == word[i]:
        i += 1
    p = p[:i]

print("Repeated substring:", p)


my_list=["Flower","flow","befl"]
p=my_list[0]

for word in my_list[1:]:
    i=0
    while i< len(p) and i<len(word) and p[i]==word[i]:
        i+=1
    p=p[:i]
print("Repeated Substring",p)