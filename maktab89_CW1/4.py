from string import ascii_lowercase
data = "The quick brown fox jumps over the lazy dog"

def pangram(s):
    alphabet = ascii_lowercase
    for i in alphabet:
        if i  not in s.lower():
            return False
    return True

print(pangram(data))