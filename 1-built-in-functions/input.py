# 1: Prompting user for an input
name = input("Enter your name\n")

# 2: or no prompt
print("Hello ", name, "! What can I do for you?", sep="")
action = input()
print("Thanks for having hope in me, but I am still under development and \
could not process your command:", action)
