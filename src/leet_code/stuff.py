def is_palidrome(word):
    return word == word[::-1]


def is_palindrome(word):
    for position in range(0, len(word)):
        if word[position] != word[len(word) - position - 1]:
            return False
    return True

print(is_palindrome("stuff"))