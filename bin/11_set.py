"""
6. Set: We have predefined/builtin option to store collection of values like list of names, list of email-ids, list of addresses etc
            - But as of now we dont know how to store
            - MUTABLE: After creating list of values, throught the program we CAN after/modify
                (we CAN add / we CAN delete / We CAN update)
            - No Index
            - No Key
            - It keeps UNIQUE values. Automatically duplicates will be removed
            - It is unordered
            - We can store only IMMUTABLE values like numbers, string, tuple etc
"""

print("Set PART-1")
print("How to store the values and print")
print("-"*20)
# --------------------

my_set_1 = {10, 10, 10, "Python", "Python", "Python", "Java", "Java"}
# internally it will create object of predefined/builtin class 'set' and store the values
# - if we provide key:value inside {} then it will become dictionary

# OR
my_set_2 = set({10, 10, 10, "Python", "Python", "Python", "Java", "Java"})

print(my_set_1, my_set_2, sep="\n")


print("#"*40, end="\n\n")
####################################

# - Since we don't have index/key, we will not be able to access each value
# - If we want index then convert to list/tuple
# - If we want key then convert to dict
# - Or we can also iterate using loops

print("Set PART-2")
print("Methods inside 'set' class")
print("-"*20)
# --------------------

print(dir(set), end="\n\n")

# OR
print(dir(my_set_1))

print("#"*40, end="\n\n")
####################################

print("Set PART-3")
print("union, intersection, difference methods")
print("-"*20)
# --------------------

sb_acc_customers = {"cust-1", "cust-2", "cust-3", "cust-4"}
loan_acc_customers = {"cust-3", "cust-4", "cust-5", "cust-6"}

print("sb_acc_customers:", sb_acc_customers)
print("loan_acc_customers:", loan_acc_customers, end="\n\n")

# union
all_customers = sb_acc_customers.union(loan_acc_customers)
print("all_customers:", all_customers)

# intersection
customers_having_both = sb_acc_customers.intersection(loan_acc_customers)
print("customers_having_both:", customers_having_both)

# Difference
customers_not_having_loan = sb_acc_customers.difference(loan_acc_customers)
print("customers_not_having_loan:", customers_not_having_loan)

print("#"*40, end="\n\n")
####################################
