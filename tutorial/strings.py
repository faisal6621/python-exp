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
str5="This string contains \new line character"
print(str5)

# 6: or treat such string as raw strings with r prefixed
str6=r"This li\ne will not break"
print(str6)

