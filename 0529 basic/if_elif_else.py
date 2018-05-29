#점수를입력받은후90점이상은A,
# 80점이상은B,
# 70점이상은C,
# 60점이상은D,
# 나머지는F로처리하는프로그램을작성하시오.

score = int(input("Enter the score\n"))

if score>=90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")