text = input('Enter a string.\n')

new_text = str()

for i in text:
    if i.isupper():
        new_text += i.lower()
    else:
        new_text += i.upper()

print('Output : '+ new_text)

print(text.swapcase())
