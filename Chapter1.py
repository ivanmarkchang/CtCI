# 1.1 Is Unique:
def unique(string):
    chars = {}
    
    for char in string:
        if char in string:
            return False
        else:
            chars[char] = True
    return True

s1 = 'abcdefg'
s2 = 'hello world'
print(unique(s1)) # True
print(unique(s2)) # False
