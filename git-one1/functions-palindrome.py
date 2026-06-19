#check whether a word is palindrome
def palindrome(word):
    y=list(word)
    for i in y:
        if i==y[i-1]:
            print("word is a palindrome")
        else:
            print("word is not a palindrome")

palindrome("kakaka")