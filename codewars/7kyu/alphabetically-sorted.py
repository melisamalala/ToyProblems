# Your task is very simple. Just write a function isAlphabetic(s), which takes an input string s in lowercase and returns true/false depending on whether the string is in alphabetical order or not.
#
# For example, isAlphabetic('kata') is False as 'a' comes after 'k', but isAlphabetic('ant') is True.
#
# Good luck :)
# https://www.codewars.com/kata/alphabetically-ordered/train/python

def alphabetic(s):
    return True if s == ''.join(sorted(s)) else False