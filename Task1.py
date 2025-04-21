"""
INPUT:
num_of_rows = 5
OUTPUT: (Please don't multiply a string with integer)
*****
*****
*****
*****
*****

"""
#Solution1:
number_of_rows=5
for i in range(number_of_rows):
    k=number_of_rows * (i+1)
    print('*****')

print("-----Task End-----")


#Solution2:
for i in range(1,6):
    k= i * (i+1)
    print('*****')

print("-----Task End-----")


