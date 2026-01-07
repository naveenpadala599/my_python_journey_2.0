c={}
with open("body.txt","r",encoding="utf-8") as f:
    for i in f.read():
        if i=="\n":
            continue
        if i in c:
            c[i]+=1
        else:
            c[i]=1
print(c)            
