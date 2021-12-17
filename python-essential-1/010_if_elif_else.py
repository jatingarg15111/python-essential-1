a=int(input("Give me a year: "))
if a<1582:
    print("Not within Gregorian Calendar")
elif a%4:
    print("common year")
elif a%100:
    print("leap year")
elif a%400:
    print("common year")
else:
    print("leap year")
