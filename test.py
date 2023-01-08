import requests

requests.get('http://google.com')
def ping(host):
    import os
    res = False

    ping_param = "-n 1" if os.name.lower() == "windows" else "-c 1"


    resultado = os.system("ping " + ping_param + " " + host)
    print(resultado)

    if resultado == 0:
        res = True
    return res

res = ping('8.8.8.8')
print(res)