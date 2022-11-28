# this is the tutoriel where we will learn how to use best formating string in python 

# How to Use %-formatting

# String objects have a built-in operation using the % operator, which you can use to format strings. Here’s what that looks like in practice:
name = "Mahamadou kheraba"
age  = 22
"hello %s, you are %s year" % (name, age)

# Why %-formatting Isn’t Great
# once you start using several parameters and longer strings, 
# your code will quickly become much less easily readable. 
# Things are starting to look a little messy already:

fristname = "Mahamadou"
secondname = "kheraba"
lastname = "diaby"
age  = 22
sexe = "Male"
profession = "developer"
"hello %s %s %s, you are %s year, sexe %s. You are %s. " % (fristname, secondname, lastname, age, sexe, profession)

# How To Use str.format()
# str.format() is improvement on %-formating
name = "Mahamadou kheraba"
age  = 22
"hello {}, you are {} year".format(name, age)

#You can reference variables in any order by referencing their index:
name = "Mahamadou kheraba"
age  = 22
"hello {0}, you are {1} year".format(name, age)

# But if you insert the variable names, 
# you get the added perk of being able to pass objects 
# and then reference parameters and methods in between the braces:

person = {'name': 'Mahamadou kheraba', 'age': '22'}
"hello {name}, you are {age} year".format(name=person[name], age=person[age])

# You can also use ** to do this neat trick with dictionaries:
person = {'name': 'Mahamadou kheraba', 'age': '22'}
"hello {name}, you are {age} year".format(**person)

# Why str.format() Isn’t Great
# str.format() can still be quite verbose when you are dealing 
# with multiple parameters and longer strings. Take a look at this

fristname = "Mahamadou"
secondname = "kheraba"
lastname = "diaby"
age  = 22
sexe = "Male"
profession = "developer"
"hello {fristname} {secondname} {lastname}, you are {age} year,sexe {sexe}. You are {profession}. ".format(fristname=fristname, secondname=secondname, lastname=lastname, age=age, sexe=sexe, profession=profession)

# f-Strings: A New and Improved Way to Format Strings in Python

# Also called “formatted string literals,” f-strings are string literals that have an f at the beginning 
# and curly braces containing expressions that will be replaced with their values

# Here are some of the ways f-strings can make your life easier.
name = "Mahamadou kheraba"
age  = 22
f"hello {name}, you are {age} year"

# It would also be valid to use a capital letter F:
name = "Mahamadou kheraba"
age  = 22
F"hello {name}, you are {age} year"