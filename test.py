import threading

balance_lock = threading.Lock()
balance_lock.acquire()
try:
    pass
finally:
    balance_lock.release()
