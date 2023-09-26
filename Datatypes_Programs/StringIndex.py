
#'index' method"

print("Strings PART-12")
print(" 'index' method")
print("-"*20)
# --------------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

result = my_string.index('E') # return index of 1st occurance of E
print("my_string.index('E'):", result)

result = my_string.index('E', 3) # return index of E BUT start looking from index 3 onwards
print("my_string.index('E'):", result)
