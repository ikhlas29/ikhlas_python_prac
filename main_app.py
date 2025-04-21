num_1=int(input("Enter 1st Number: "))
num_2=int(input("Enter 2nd Number: "))
operation=input("Select + or - or *: ")
result=0

if operation=="+":
    result=num_1+num_2
elif operation=="-":
    result=num_1-num_2
elif operation=="*":
    result=num_1*num_2
print("Result is:", result)