T_h=int(input("Give me the start time(hour): "))
T_m=int(input("Give me the start time (minute): "))
T_d=int(input("Give me the duration in minutes: "))
T_d=(T_h*60)+T_m+T_d
print("The finish time is: ",end="")
print(T_d//60,T_d%60,sep=":")
