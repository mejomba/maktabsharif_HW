from log_module import logger_fib, logger_prime, logger_console


def fibonacci_of(n):
    try:
        if n < 0:
            raise ValueError(f'{n} is not valid input range(2, inf)')
        if n in {0, 1}:
            return n
        return fibonacci_of(n - 1) + fibonacci_of(n - 2)
    except ValueError as err:
        logger_fib.error(err)
    except Exception as err:
        logger_console.warn(err)


def is_prime(n):
    try:
        if n <= 1:
            raise ValueError(f'{n} is not valid input range(2, inf)')
        for i in range(3, n):
            if n % i == 0:
                return False
        return True
    except ValueError as err:
        logger_prime.error(err)


# print(is_prime(-2))
# fibonacci_of(-5)
logger_console.debug('salam')
logger_console.warning('salam')
logger_console.warning('salam')
logger_console.warning('salam')



