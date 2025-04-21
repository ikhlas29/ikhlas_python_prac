num_1=int(input("Enter 1st Number: "))
num_2=int(input("Enter 2nd Number: "))
operation=input("Select + or - or * or / or ** or ! (factorial) or absolute or | (OR) or & (AND) or ^ (XOR): ")
result=0

if operation=="+":  #Addition
    result=num_1+num_2

elif operation=="-":  #Subtraction
    result=num_1-num_2

elif operation=="*":  #Multiplication
    result=num_1*num_2

elif operation=="/":   #Division
    result=num_1/num_2

elif operation=="**":  #Power
    result=num_1**num_2

elif operation=="!":  #Factorial
    result=1
    for i in range(1,num_1+1):
        result=result*i

elif operation=="absolute":  #Absolute
    result=abs(num_1)

elif operation=="|":  #OR
    result=num_1|num_2

elif operation=="&":  #AND
    result=num_1 & num_2

elif operation=="^":  #XOR
    result=num_1 ^ num_2
    
print("Result is:", result)