inpStr = input("Enter Word:\n").upper()
reverseInpStr = inpStr[::-1]

if inpStr == reverseInpStr:
    print("This is a Palindrome!")

elif inpStr != reverseInpStr:
    print("This is not a Palindrome!")

else:
    print("unknown error!")