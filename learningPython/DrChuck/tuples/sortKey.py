c = { "a":10, "b":1 , "c":22}
tmp = list()
for k,v in c.items():
    tmp.append( (v , k) )#insert the key and its value like tuple in the tmp list

print(sorted(list(c.items()), reverse=True))
#sort by key
tmp = sorted(tmp , reverse=True)
print(tmp)
