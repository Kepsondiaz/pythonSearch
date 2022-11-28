# this is the tutoriel where we will learn how to use best formating string in python 

# How to Use %-formatting

# String objects have a built-in operation using the % operator, which you can use to format strings. Here’s what that looks like in practice:
name = "Mahamadou kheraba"
age  = 22
"hello %s, you are %s year" % (name, age)

# Why %-formatting Isn’t Great

fristname = "Mahamadou"
secondname = "kheraba"
lastname = "diaby"
age  = 22
sexe = "Male"
profession = "developer"
"hello %s %s %s, you are %s year, sexe %s. You are %s. " % (fristname, secondname, lastname, age, sexe, profession)