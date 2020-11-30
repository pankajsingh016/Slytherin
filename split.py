#The Program will take the name and find the most common letter in your name
name = input('Enter your name -:')
ls = list(name)
mc = dict()
for i in ls:
    mc[i] = mc.get(i,0)+1

print(mc)
let=None
count=0
for l,y in mc.items():
    if y>count or count == 0:
        count=y
        let =l
print("The Most Frequent Letter in your name is -:",let,count,"times.")



