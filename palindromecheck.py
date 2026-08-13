string=str(input("enter a string:"))
lst=[ch for ch in string]

st,end=0,len(lst)-1
while st<end:
    lst[st],lst[end]=lst[end],lst[st]
    st+=1
    end-=1
rev=""
for ch in lst:
    rev+=ch
if string==rev:
    print("palimdrome")
else:
    print("not")