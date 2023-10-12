#convert existind string to RAW FORMAT:

print("Strings PART-3")
print("How to store and print")
print("-"*20)

a = "C:\newfolder\test.py"
# By default, inside string, we are using \with some characters for special purpose
# examplE: \n-> replace with new line \t> replace with tab space

#if we want as \n\t as it is then
b = "C:\newfolder\test.py"
# r-> raw string, dont replace \n\t etc

print("a:",a)
print("b:",b)
print("convert existind string 'a' to RAW FORMAT:", repr(a))
print("convert existind string 'b' to RAW FORMAT:", repr(b))
