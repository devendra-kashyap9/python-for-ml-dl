### Multithreading
## When to use Multi Threading
# I-O bounded task: task that spend more time waiting for I/O operation (e.g. file operation, 
#                                                                                          network requests)
# Concurrent execution : When we want to improve the throughput of our application by performing
#                                                                   multiple operation concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")
        
def print_letters():
    for letter in "letters":
        time.sleep(2)
        print(f"Letter: {letter}")
        
# create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
 
start = time.time()  

# starting the threads   
t1.start()
t2.start()

# wait for thread to complete
t1.join()
t2.join()

end = time.time() - start
print(end)
