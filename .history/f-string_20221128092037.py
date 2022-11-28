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