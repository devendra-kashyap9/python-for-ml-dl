'''
Real World Example: MultiProcessing for CPU bound task.
Scenario: Factorial Calculation
Factorial calculation specially for large numbers, involve significant computation wotk. Multiprocessing 
can be used to distribute the workload across multiple CPU cores to improve performance.
'''

import sys
import math
import time
import multiprocessing

# Increase the maximum number of digits for integer coversion
sys.set_int_max_str_digits(100000)

# function to compute factorial of given number
def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    
if __name__ == '__main__':
    numbers = [5000, 6000, 7000, 8000]
    
    start = time.time()
    
    # create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial, numbers)
        
    end = time.time()
    
    print(f"Results: {results}")
    print(f"Time taken: {end - start} seconds")