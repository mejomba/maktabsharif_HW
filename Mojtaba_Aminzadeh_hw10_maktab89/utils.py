import requests
from hangman import Bank
import os


def is_connect(host):
    res = False

    if 'nt' in os.name.lower():
        exit_code = os.system(f"ping -n 1 {host} > clear;rm clear")
    else:
        exit_code = os.system(f"ping -c 1 {host} > clear;rm clear")

    if exit_code == 0:
        res = True
    return res


def request_to_api():
    return requests.get(f"{Bank.api}",
                        headers={'X-Api-Key': f"{Bank.api_key}"},
                        params={type: 'noun'})

