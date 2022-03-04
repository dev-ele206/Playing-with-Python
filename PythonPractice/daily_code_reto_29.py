s = input("Enter a word and I'll tell you if its a palindrome: ")

def isPalindrome(s):
    return s == s[::-1]

response = isPalindrome(s)

if response:
    print(f"{s} is a palindrome!")
else:
    print(f"{s} is not a palindrome!")