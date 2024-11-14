marks=int(input('enter marks:'))
if(marks>90):
    print("distant")
elif(marks>75):              #if checks every condition where as elif checks only that condition and not check below conditions
    print("first grade")
elif(marks>60):
    print("second grade")
elif(marks>27):
    print("third grade")
else:
    print("fail")