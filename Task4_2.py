def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated
    elif len(L) > 1:                                  #   and what are the values being added? First, the lengths of the first 3 words in the list
        result = len(L[0]) + len(L[1])                # For which call below is this statement evaluated
    elif len(L) > 0:                                  #   and what are the values being added? 3rd, lengths of the first 2 words
        result = len(L[0])                            # For which call below is this statement evaluated
    else:                                             # and what are the values being added? Second, the length of the first term in the list
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()
