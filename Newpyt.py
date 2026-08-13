#reversing a string
str="hello"
lst =[]
for ch in str:
    lst.append(ch)
st=0
end=len(lst)-1
while st<end:
    lst[st],lst[end]=lst[end],lst[st]
    st+=1
    end-=1
result=""
for ch in lst:
    result+=ch
print(result)

        

