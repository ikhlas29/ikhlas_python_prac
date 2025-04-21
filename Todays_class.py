
for i in range(1,6):
    k= i * (i+1)
    print('*****')

print("-----Task End-----")










33333
#Solution1
num_of_rows = 5   #setting the numbers of rows

for i in range(num_of_rows): #for the outter loop that start from i=0 to i=4 (5 items)
    for spaces in range(2 * i + 1):  #formula to print the spaces (inner loop)
        print("*" , end='')
        #exaple: row0 = 1 star ----> 2*0+1= 1 
    for stars in range(2 * i -1):  #formula to print the stars (inner loop)
        print("*" , end='')   
        #example for i=0 ---> 2*0-1=null
                
print() # To move to the next line

print("----Task End----")