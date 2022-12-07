n=int(input("n:"))
i=1
a=0
b=0
while i<=n :
    if (i%2==0):
        a=a+1
    else:
        b=b+1
    i=i+1    
print(" even number between 1 to",n,"is",a)
print(" odd number between 1 to",n,"is",b)
