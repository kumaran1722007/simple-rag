data=[]
with open('cat-facts.txt', 'r') as file:
    data=file.readlines()
    print(f"loaded {len(data)} entities")
    print(data,end="")
