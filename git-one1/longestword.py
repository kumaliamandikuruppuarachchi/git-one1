def longestword(*word):
    '''this finds the longest word from a list'''
    i=0
    for a in word:
        if len(a)>i:
            longest_word=a
            i=len(a)
    return(longest_word)
y=longestword("balla","pusa","haraka")
print(y)