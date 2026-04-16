def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point? this is confusing code
         # What are the values of first and second at this point? first: this is confusing code avoid, second: this is confusing code avoid such
         # What happened?
print()