c=0
n=int(input("Enter any integer: "))
for m in range(2,n//2+1):
      if n%m==0:
          c=c+1
          break
if c>0:
 print("This is a composite number.")
else:
    print("This is a prime number.")
print("The end.")
