# 10 len()
# 2 upper
# 1 digit
# 1 symbol

from string import printable
import random
from functools import reduce


digits = printable[:10]
lower_case = printable[10:36]
upper_case = lower_case.upper()
symbol = printable[62: 94]

password = random.sample(upper_case, k=2) + random.sample(digits, k=1) + random.sample(symbol, k=1) + random.sample(printable[:94], k=6)
print(password)
password = reduce(lambda x, y: x + y, password)
print(password)

