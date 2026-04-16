def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # For which calls below is this statement evaluated? Answer: if smallest is true, L3, otherwise L5
    else:
        return m

first = smallest(3, 2)       # What is the value of first? answer: 2
second = smallest(2, 2)      # What is the value of second? Is this a reasonable result? Why or why not? answer: 2, yes because the smallest number is 2, even if both vales are the same
print()
