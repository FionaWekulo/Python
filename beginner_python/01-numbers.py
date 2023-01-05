#age is a variable
age = 25
print(age)
print(age+10)


#this is a comment
#below if a multi line comment
"""
print(age)
"""


#how to create variables
age1 = 1
age_2 = 2
#invalid name -> age-3 = 3
#invalid name -> 4age = 4
#Age = 6 #not recommended
age_of_user = 7 #recommend underscores for multiple words based on this guide:
#https://www.python.org/dev/peps/pep-0008/#function-and-variable-names
#return = 5 --> Cannot assign keywords as variable names
#https://docs.python.org/3/reference/lexical_analysis.html#keywords


########## OPERATORS ##########
result = 20 / 3 #6.6666....
print(result) 
print("Here is a floor version (crop decimal):", 20 // 3) #6
import math
new_result = math.floor(result)
print(new_result)
newer_result = math.ceil(result)
print(newer_result)

#remainder
modulus=(10%3)
print(modulus)

#raising a number to a power (5^)
result = 5**2
print(result)
power=math.pow(5,2)
print(power)

#You can use round instead. 
print(round(20/3), 0)

