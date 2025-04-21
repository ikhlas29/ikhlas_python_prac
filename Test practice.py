
#Question1 solution:
"""
size= int(input("Input the size: "))
for i in range(size):
    if i==0 or i==size-1:
           print('*' * size)

    else:
        print('*' + ' ' * (size-2) + '*')
"""



#Question2 solution:to complete
"""
size=5
for i in range(size):  
    for spaces in range(size - i - 1):  
        print(' ', end='')

    for num in range(2 * i + 1):   
        print(num+1, end='')   
    print()
"""
menu_options = {
    1: 'Print Pattern',
    2: 'Rotate Array ',
    3: 'Help',
    4: 'Exit',
}
 
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
        
def print_pattern():
    n=''
    n = int(input('Enter the number of rows for the pattern: '))
 
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()
 
def filter_numbers():
    try:
        n = int(input("Enter the number of elements (n): "))
        k = int(input("Enter the number of steps (k): "))
        elements = list(map(int, input("Enter the array elements separated by spaces: ").split()))
        num = []
        for i in range(n-k, n):
            num.append(elements[i])
        for i in range(0, n-k):
            num.append(elements[i])
        print("Rotated array: ", num)
    except ValueError:
        print("Invalid input. Please enter valid integers for n, k, and array elements.")
    
    
# except ValueError:
#     print("Invalid input. Please enter valid integers for n, k, and array elements.")
 
def help_option():
     print('''Option 1: Print a pattern with 'n' rows of decreasing asterisks.
Option 2: Rotate an array of 'n' elements of the right by 'k' steps.
Option 3: Display this help message.
Option 4: Exit the program.''')
        
def exit_option():
    print('Exiting the program. Goodbye!')
    exit()  # This will terminate the program immediately
 
def main():
    while(True):
        print("\nWelcome to the Menu-Based Program!")
        print_menu()
        option = ''
        try:
            option = int(input('Please select an option: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           print_pattern()
        elif option == 2:
         filter_numbers()
        elif option == 3:
            help_option()
        elif option == 4:
            exit_option()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
if __name__=='__main__':
    main()










