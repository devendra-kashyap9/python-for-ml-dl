# Multiprocessing with thread pool executor

import time
from concurrent.futures import ProcessPoolExecutor

def print_squares(number):
    time.sleep(3)
    return f"Squares; {number * number}"

numbers = [1,2,3,4,5,6,7,8,9,1,2,0,11,16]


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_squares, numbers)
        
    for result in results:
        print(result)