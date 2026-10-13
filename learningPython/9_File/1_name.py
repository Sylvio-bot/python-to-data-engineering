name = input("what 's your name? ")
#w : write no save
#a: append
'''
file = open("names.txt","a")
file.write(f"{name} \n")
file.close()
'''
'''
with open("names.tex","a") as file:
    file.write(f"{name} \n")
'''
with open("names.txt","r") as file:
    lines =  file.readlines()#return a list

for line in lines :
    print(f"hello {line} ")

