# def ping(host):
#     """
#     Returns True if host responds to a ping request
#     """
#     import subprocess, platform
#
#     # Ping parameters as function of OS
#     ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
#     args = "ping " + " " + ping_str + " " + host
#     need_sh = False if  platform.system().lower()=="windows" else True
#
#     # Ping
#     return subprocess.call(args, shell=need_sh) == 0
#
# # test call
# res = ping("8.8.8.8")

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