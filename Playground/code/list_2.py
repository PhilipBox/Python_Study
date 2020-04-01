star = []
num = 0
while num<5:
    read_num = (int)(input('Enter the number of star(1~30) '))
    if(read_num>=1 and read_num<=30):
        star.append(read_num)
        num +=1
    else:
        pass

for i in range(0,5):
    count = star[i]
    for j in range(0,count):
        print('*', end='')
    print('')

