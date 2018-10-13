#  Exclamation marks series 4: Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string

# Description:
# Remove all exclamation marks
# from sentence but ensure a exclamation mark at the end of string.
# For a beginner kata, you can assume that the input
# data is always a non empty string, no need to verify it.


# url: https://www.codewars.com/kata/exclamation-marks-series-number-4-remove-all-exclamation-marks-from-sentence-but-ensure-a-exclamation-mark-at-the-end-of-string/train/python

# Video to my Solution: https://www.youtube.com/watch?v=F4j1WRduSAQ&t=25s

def remove(s):
    s = s.replace("!", "")
    s += "!"

    return s