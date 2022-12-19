
from importlib import resources
...
# read text file
with resources.open_text('testpakage', 'somefile.txt') as fp:
    txt = fp.read()
...
# or binary
with resources.open_binary('testpakage', 'image1.jpeg') as fp:
    img = fp.read()