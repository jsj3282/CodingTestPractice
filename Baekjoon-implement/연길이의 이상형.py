MBTI = {
    "E" : "I",
    "S" : "N",
    "T" : "F",
    "J" : "P",
    "I" : "E",
    "N" : "S",
    "F" : "T",
    "P" : "J"

}

yg = str(input())

for i in yg:
    print(MBTI[i], end="")
