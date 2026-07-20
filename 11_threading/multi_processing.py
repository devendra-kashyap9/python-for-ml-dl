### MultiProcessing
## Multiprocessing is a concurrency model where an application spawns completely separate, 
# independent Operating System processes —each running its own Python interpreter instance and 
# occupying a distinct space in memory.
## Unlike Multithreading, which runs multiple threads inside a single process and is bound by
# Python's Global Interpreter Lock (GIL), Multiprocessing side-steps the GIL entirely. 
# This allows true simultaneous execution across multiple physical CPU cores.

## Multiprocessing allows us to create processes which can run in parallel.
# CPU Bound task - task that are heavy on CPU (e.g. mathematical computation)
# Parallel Execution - Using Multiple Cores of CPU.

import time
import multiprocessing

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")
        
def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i*i*i}")

# entry point
if __name__ == '__main__':
    # create two processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()

    # start the processes
    p1.start()
    p2.start()

    # wait for the processes to complete
    p1.join()
    p2.join()

    end = time.time() - t
    print(end)