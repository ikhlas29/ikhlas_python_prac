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

#Solution1:

num_of_rows = 5 #setting the numbers of rows
for i in range(num_of_rows):   #for the outter loop that start from i=0 to i=4 (5 items
    for spaces in range(num_of_rows - i - 1):  #formula to print the spaces (inner loop)
        print(' ', end='')
        #exaple: row0 = 1 star ----> 2*0+1= 1 
    for stars in range(2 * i + 1):   #formula to print the stars (inner loop)
        print('*', end='')   
        #example for i=0 ---> 2*0-1=null
    print() #to move to the next line 

print("----Task End----")
print()
print()
print()




#Solution2: 
#using range without defining the numbers of rows 

for i in range(0,5):  
    for spaces in range(0,5 - i - 1):  
        print(' ', end='')
         
    for stars in range(2 * i + 1):   
        print('*', end='')   
    print()  

print("----Task End----")
print()
print()