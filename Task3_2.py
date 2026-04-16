def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             # In general, when will a call to this function evaluate this statement?
    elif b > c:                  # answer: when the first value is the largest number
        return b + c             # In general, when will a call to this function evaluate this statement?
    else:                        # answer: when the 2nd value is the largest number
        return 2 * c             # In general, when will a call to this function evaluate this statement?
                                 # answer: when the 3rd value is the largest number

answer1 = function2(3, 2, 1)     # What is the value of answer1? 1
answer2 = function2(2, 3, 1)     # What is the value of answer2? 4
answer3 = function2(2, 1, 3)     # What is the value of answer3? 6
print()