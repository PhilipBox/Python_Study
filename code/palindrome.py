text = input('Enter a string : ')

origin = text.replace(' ', '')

reverse = str()

index = len(origin)-1

while index >= 0:
    reverse += origin[index]
    index -= 1

if origin == reverse:
    print('This is a palindrome.')
else:
    print('This is not a palindrome.')