import re

def check_character(string):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)

print(check_character('ASAADAFFADFAqgfqhdqjywe327380'))
print(check_character('*&$#)!&#$H!K!@#G)!@&*#!#B!@'))