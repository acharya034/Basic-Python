print("This is a fabonacci numbers generator.")
n=int(input("Up to what number you want fabonacci numbers.\n\t -->"))
j=0
i=0
k=1
while i < n:
    print(i,end =", " if i<n else "")
    i+=k
    k=j
    j=i