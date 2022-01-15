I=float(input("Enter any natural number: "))
a=0
b=1
if(I%1==0 and I>0):
    while(I//b>=1):
        a+=1
        b=b*10
    print("The total number of digit is: ",a)
else:print("This is not a natural number.")
