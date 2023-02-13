import logging


logger_fib = logging.getLogger('fib_logger')
logger_prime = logging.getLogger('prime_logger')
logger_console = logging.getLogger('console_logger')

logger_console.propagate = False

FORMAT12 = logging.Formatter('%(levelname)s - %(asctime)s - %(module)s:%(lineno)d %(message)s')
FORMAT3 = logging.Formatter('%(levelname)s - %(asctime)s - %(message)s')

fib_handler = logging.FileHandler('fib.log')
prime_handler = logging.FileHandler('prime.log')
console_handler = logging.StreamHandler()

fib_handler.setLevel(logging.ERROR)
prime_handler.setLevel(logging.ERROR)
console_handler.setLevel(logging.DEBUG)

fib_handler.setFormatter(FORMAT12)
prime_handler.setFormatter(FORMAT12)
console_handler.setFormatter(FORMAT3)

logger_fib.addHandler(fib_handler)
logger_prime.addHandler(prime_handler)
logger_console.addHandler(console_handler)
