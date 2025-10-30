# Random Password Generator using Python

#import the necessary libraries
import random
import string

#input the length of the password
length = int(input("Enter the length of the password: "))

#Define data to be used in the password
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation   

#combine the data
all = lower + upper + numbers + symbols

#use random to generate the password
password = "".join(random.sample(all, length))

#print the password
print("Your password is: ", password)

