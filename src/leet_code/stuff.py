import time

def is_palindrome(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome(word):
    for position in range(0, len(word)):
        if word[position] != word[len(word) - position - 1]:
            return False
    return True

word = "stuff"

measure = time.process_time()
print(f"{is_palindrome(word)} {measure}")



