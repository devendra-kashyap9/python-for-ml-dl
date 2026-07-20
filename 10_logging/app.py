import logging

# logging settings
logging.basicConfig(
    level=logging.DEBUG, # Capture EVERYTHING from DEBUG level up
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithemeticApp")

def add(a, b):
    result = a + b
    logger.debug(f"The sum of {a} + {b} is {result}")
    return result

def sub(a, b):
    result = a - b
    logger.debug(f"The difference of {a} - {b} is {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"The product of {a} * {b} is {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"The sum of {a} / {b} is {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
 
# driver code   
add(10, 15)
sub(15, 10)
multiply(10, 20)
divide(10, 20)
divide(20, 0)
