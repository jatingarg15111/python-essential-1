n=int(input("Enter any natural number: "))
for m in range(1,n//2+1):
    if n%m==0:
        print(m,end=", ")
print(n)
print("The end.")
