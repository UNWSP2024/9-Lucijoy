# Author: Lucia Floan
# Date: Mar 28, 2025
# Title: Item Counter
# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    try:
        with open('names.txt', 'r') as file:
            lines = file.readlines()

        if lines:
            print (f'{len(lines)} names were found')
            print ('the names are:')
            for name in lines:
                print(f'- {name}')
        else:
            print('file is empty.')

    except FileNotFoundError:
        print("the file 'names.txt' does not seem to exist.")
    except Exception as e:
        print(f'something went wrong: {e}')
    
    ######################
    print('In the count_file_lines function')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
