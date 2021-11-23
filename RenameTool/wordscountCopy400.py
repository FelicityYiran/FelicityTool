# 词频统计

def getText():
    txt = open("English.txt","r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+_,./?;:<>@\\~{}|[]':
        txt = txt.replace(ch," ")
    return txt

myTxt = getText()

words = myTxt.split()

counts = {}

for word in words:
    counts[word] = counts.get(word,0) + 1

items=list(counts.items())

items.sort(key = lambda x:x[1],reverse = True)

with open("countwords.txt","w") as result:
    for i in range(500):
        word,count =  items[i]
        result.write("{0:<10}|{1:>5}\n".format(word,count))
         
            

    