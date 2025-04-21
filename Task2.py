"""

INPUT:
num_of_rows = 5
OUTPUT: (Please don't multiply a string with integer)
*
***
*****
*******
*********

"""
#Solution1
number_of_rows=5
for i in range(number_of_rows):
    for j  in range(2 * i + 1):
        print('*',end='')
    print()
print("-----Task End-----")


#Solution2 using range 
for i in range(0,5):
    for j  in range(2 * i + 1):
        print('*',end='')
    print()
print("-----Task End-----")