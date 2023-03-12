# 1.1 Is Unique: determine if string has all unique characters.
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

# 1.2 Check Permutation: given 2 strings, determine if one is a permutation of the other.
def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    return sorted_s1 == sorted_s2

s1 = 'abcd'
s2 = 'dcba'
s3 = 'abc'
print(is_permutation(s1, s2)) # True
print(is_permutation(s1, s3)) # False

# 1.3 URLify: replace all spaces with '%20'.
def replace_spaces(s):
    new_s = ''
    
    for c in s:
        if c == ' ':
            new_s += '%20'
        else:
            new_s += c
    return new_s

s = 'hello_world'
print(replaces_spaces(s))

# 1.4 Palindrome Permutation: given a string, check if it is a permutation of a palindrome.
