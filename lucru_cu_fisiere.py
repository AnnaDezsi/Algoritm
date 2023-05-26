file=open('D:\\Dezsi Anna Alexa\\pycharm.txt','r+')
print(file.read)
print(file.tell)
el =[]
for line in file:
   el.append(line)
   print(el)
file.close()
while i<len(el) :
    if el[i].startswith("4"):
        el.insert(i,'3333\n')
        i+=1
    i+=1
print(el)
file=open('D:\\Dezsi Anna Alexa\\pycharm.txt','w+')
for e in el:
    file.write(e)
file.close()