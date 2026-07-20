from logger import logging

def add(a,b):
    logging.debug('Adiition operation...')
    return a+b

logging.debug('The add function is called...')
add(10,15)