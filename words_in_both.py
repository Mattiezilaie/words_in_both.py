# Author: Mahtab Zilaie
# Date: November 19 2019
# Description: A function that takes two string parameters and returns a set
# of words in both strings in lower case

def words_in_both(s1,s2):
    """takes two string parameters and returns a set of the
    words (in lower case)contained in both strings
    -capitalization doesn't matter"""
    words1 = s1.lower().split(" ")
    words2 = s2.lower().split(" ")
    return {i for i in words1 if i in words2}

