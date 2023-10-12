#STEP VALUE: We can skip characters

print("Strings PART-7")
print("STEP VALUE: We can skip characters")
print("-"*20)
# --------------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx Section-3
print("Substring from index 1 to 6 using + ve index no default step by '1':", my_string[1:6])
print("Substring from index 1 to 6 using - ve index no default step by '1':", my_string[-7:-2], end="\n\n")
# By default Step Value=1
# Which means, from 1 to 6 give me every character

print("Substring from index 1 to 6 using + ve index no step by '1':", my_string[1:6:1])
print("Substring from index 1 to 6 using - ve index no step by '1':", my_string[-7:-2:1], end="\n\n")
# Step Value=1
# Which means, from 1 to 6 give me every character

print("Substring from index 1 to 6 using + ve index no step by '2':", my_string[1:6:2])
print("Substring from index 1 to 6 using - ve index no step by '2':", my_string[-7:-2:2], end="\n\n")
# Step Value=2
# Which means, from 1 to 6 give me every 2nd character
# by default, character at start index will always come, after that every 2nd character
