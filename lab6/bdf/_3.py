def is_palindrome(string):
    if string == string[::-1]:
        return "YES"
    else:
        return "NO"

word = "madam"
print(is_palindrome(word))