# https://docs.python.org/3/tutorial/introduction.html#strings
# 1: String in python either enclosed in double quotes (" ")
str1 = "\"A double quoted string\""

# 2: or in single quotes (' ')
str2 = '\'A single quoted string\''

print(str1)
print(str2)

# 3: an escap character (\) is used if you are using " within double quoted
# string or vice versa
# - In above example we have used the escape charater

# 4: but you do not need to escape ' within double quoted string and vice
# versa

str3 = "\"A ' not needed to be escaped in double quotes\""
str4 = '\'A " not needed to be escaped in single quotes\''

print(str3)
print(str4)

# 5: \ is not just to escape quotes, it has other meanings too. 
# e.g., \n means a new line and if used within string will break it to two
# lines
str5 = "This string contains \new line character"
print(str5)

# 6: or treat such string as raw strings with r prefixed
str6 = r"This li\ne will not break"
print(str6)

# 7: String literals can span multiple lines using triple quotes (""" or ''')
# new line characters automatically included but can be prevented by using \
str7 = """\
    {
      name: "John", \
      age: 31, \
      city: "New York"
    }"""
print(str7)

# 8: strings can be concatenated with +
str8 = str1 + str2
print(str8)

# 9: string literals can be concatenated putting next to each other
str9 = "Hello " 'World'
print(str9)

# 10: strings can be repeated with *
print(3 * "Hello World")

# 11: a character is simply a string of size one. no special character types
print(str9[0], str9[6])

# 12: negative index of string will pick character from last
print(str9[-1], str9[-7])

# 13: slicing a string
print(str9[0:5]) # from index 0 (included) to 5 (excluded)
print(str9[6:11]) # from index 6 (included) to 11 (excluded)
print(str9[:5]) # omitting left of : will slice from begining to 5 (excluded)
print(str9[6:]) # omitting right of : will slice from 6 (included) to the end

