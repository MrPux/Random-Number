#   Define a function, 'random_number', that takes no parameters. 
#   The function must generate a random integer between 1 and 100, both inclusive and return it.

#Calling the function multiple times should (usually) return different numbers.

#E.g, calling random_number some times might firsr return 42, then 63, then 1. 
import random

def random_number():
    return random.randint(1, 100) 