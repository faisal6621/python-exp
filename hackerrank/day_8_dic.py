# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/forum
N = int(input())  # number of entries
phonebook = {}
for i in range(N):
    line = str(input()).split()
    phonebook[line[0]] = line[1]

# print(phonebook)
name = input()
while name:
    if name in phonebook:
        print(name, phonebook[name], sep='=')
    else:
        print('Not found')
    name = input()
