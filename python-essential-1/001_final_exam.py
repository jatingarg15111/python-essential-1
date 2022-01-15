secret_number=777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
|So, what is the secret number?  |
+================================+
""")

x=0
n=1
while n>0:
    n=int(input("Enter an integer number: "))
    if n==secret_number:
        print("\"Well done, muggle! You are free now and you guessed in",x+1,"tries.\"")
        break
    elif n!=secret_number:
        if n>secret_number:
           print("\"Ha ha! You're stuck in my loop! the secret number is greater than your guess. \"")
        else:print("\"Ha ha! You're stuck in my loop! the secret number is less than your guess. \"")
        x+=1    




