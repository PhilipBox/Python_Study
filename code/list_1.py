score = []
num = 0

while num<10:
    read_num = (int)(input('Enter your score(0~100) '))
    if(read_num>=0 and read_num<=100):
        score.append(read_num)
        num+=1
    else :
        pass

print(score)

min = min(score)
max = max(score)

score.remove(min)
score.remove(max)
print(score)

AVG = sum(score) / len(score)

print("AVG : ", AVG)
print("MAX : ", max)
print("MIN : ", min)