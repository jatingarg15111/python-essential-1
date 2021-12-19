e=0
o=0
n=1
while n!=0:
    n=int(input("Enter any number: "))
    if n%2==0:
        e=e+1
    else:
        o=o+1
print("The number of even numbers: ",e-1)
print("The number of odd numbers: ",o)
print("The end.")
