#Substring from index

print("Strings PART-6")
print("SLICING: We can get substring")
print("-"*20)
# --------------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx Section-2
print("Substring from index 1 to 6 using + ve index no:", my_string[1:6])
print("Substring from index 1 to 6 using - ve index no:", my_string[-7:-2])
print("Substring from index 1 to 6 using + ve/-ve index no:", my_string[1:-2])
print("Substring from index 1 to 6 using + ve/-ve index no:", my_string[-7:6], end="\n\n")

print("Substring from index 1 to END using + ve index no:", my_string[1:])
print("Substring from index 1 to END using - ve index no:", my_string[-7:], end="\n\n")

print("Substring from BEGINNING to 6 using + ve index no:", my_string[:6])
print("Substring from BEGINNING to 6 using - ve index no:", my_string[:-2])

print("Substring from BEGINNING to END :", my_string[:])
