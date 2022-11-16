rowNum = int(input("Enter number of rows you want:\n"))
patternType = int(input("Enter 0 for increasing pattern and 1 for decreasing pattern:\n"))

if patternType == 0:
    for i in range(1, rowNum + 1):
        print("*" * i , end ="\n")

elif patternType == 1:
    for i in range(rowNum, 0, -1):
        print("*" * i , end ="\n")
