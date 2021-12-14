T_h=int(input("Give me the start time(hour): "))
T_m=int(input("Give me the start time (minute): "))
T_d=int(input("Give me the duration in minutes: "))
T_r=(T_h*60)+T_m+T_d
print("The finish time is: ",end="")
print(T_r//60,T_r%60,sep=":")
