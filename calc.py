num_1=int(input("Enter 1st Number: "))
num_2=int(input("Enter 2nd Number: "))
operation=input("Select + or - or * or / or ** or ! (factorial): ")
result=0

if operation=="+":
    result=num_1+num_2
elif operation=="-":
    result=num_1-num_2
elif operation=="*":
    result=num_1*num_2
elif operation=="/":
    result=num_1/num_2
elif operation=="**":
    result=num_1**num_2
elif operation=="!":
    result=1
    for i in range(1,num_1+1):
        result=result*i

print("Result is:", result)