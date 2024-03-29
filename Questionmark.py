#Have the function QuestionsMarks(str) take the str string parameter, which will contain single
# digit numbers, letters, and question marks, and check if there are exactly 3 question marks between
# every pair of two numbers that add up to 10. If so, then your program should return the string true, 
# otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the 
# string, then your program should return false as well.

def QuestionsMarks(str):
    a = 11
    b = 'false'
    c = 0
    for i in str:
        if i.isdigit():
            if int(i) + a == 10:
                if c != 3:
                    return 'false'
            b = 'true'
            c = 0
            a = int(i)
        elif i == '?':
            c += 1
    return b
# keep this function call here 
print(QuestionsMarks(input()))
