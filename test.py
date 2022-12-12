import threading


class Singleton:
    __lock = threading.Lock()
    __instance = None

    @classmethod
    def instance(cls):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = cls()


A = Singleton.instance()
B = Singleton.instance()
print(A)
print(B)

