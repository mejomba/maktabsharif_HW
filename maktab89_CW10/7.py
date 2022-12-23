import re

text = 'f_gd_fb_dfb_fsdg_dbbb'
pattern = r'[a-z]+(?:_[a-z]+)+$'
result = re.findall(pattern, text)
print(result)



