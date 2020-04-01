accusation = {'room':'ballroom', 'weapon':'lead pipe', 'person':'Col.Mustard'}

for key in accusation:
    print(key)

print('--------------------')

for val in accusation.values():
    print(val)

print('--------------------')


for key,val in accusation.items():
    print('Key is', key, '// value is :', val)
