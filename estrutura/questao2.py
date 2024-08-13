def is_palindrome(string):
    string = string.lower().replace(" ", "")
    
    stack = []
    
    for char in string[:len(string)//2]:
        stack.append(char)
    
    if len(string) % 2 != 0:
        # Se tiver, ignora o caractere central
        string = string[len(string)//2 + 1:]
    else:
        string = string[len(string)//2:]
    
    for char in string:
        if char != stack.pop():
            return False
    
    return True

print(is_palindrome("Ame a ema"))
print(is_palindrome("hello"))