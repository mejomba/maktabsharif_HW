import re


RED = "\033[0;31m"
GREEN = "\033[0;32m"
END = "\033[0m"


# text = "Iran (Persian: ایران Irān [ʔiːˈɾɒːn] (About this soundlisten)), also called Persia[11] and officially the"
text = "dsfdsfASDFFD21651dsf132"
pattern = r"[^A-Z\d]+"

if not re.search(pattern, text, flags=re.I):
    print(f"{GREEN}{text}{END} is valid format")
else:
    print(f"{RED}{text}{END} is invalid format")
