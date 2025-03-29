# Author: Lucia Floan
# Date: Mar 28, 2025
# Title: Average Numbers
# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    ######################
    try:
        with open('numbers.txt', 'r') as file:
            lines = file.readlines()
        total = 0
        for line in lines:
            try:
                total += int(line.strip())
            except ValueError:
                print(f'moving on from invalid value: {line.strip()}')

        print(f'the total sum is: {total}')

    except IOError:
        print('Something went wrong with reading the file.')
    except Exception as e:
        print(f'Something went wrong, an error occured: {e}')
    ######################
    print('In the sum_numbers_from_file function')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()
