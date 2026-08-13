lst=[1,1,2,2,3,3,4,5]
new_list=[]
for el in lst:
    if el in new_list:
        continue
    else:
        new_list.append(el)
print(new_list)

