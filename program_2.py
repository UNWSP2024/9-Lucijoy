# Author: Lucia Floan
# Date: Mar 28, 2025
# Title: Random Number File Writer
# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random 

def random_numbers():
  numbers_to_generate = int(input('Choose amount of random numbers to generate: '))
  if numbers_to_generate < 1 or numbers_to_generate > 1000:
    print('Enter a different number between 1 and 1000.')
    return

  random_num = []
  for i in range(numbers_to_generate):
    random_num.append(random.randint(1,500))

  with open('random_numbers.txt', 'w') as file:
    for num in random_num:
      file.write(str(num) + '\n')
  print (f"{numbers_to_generate} random numbers have been written into 'random_numbers.txt'.")

if __name__ == '__main__':
    random_numbers()
               
