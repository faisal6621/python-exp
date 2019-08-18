# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/
def openOrSenior(data):
    result = []
    for item in data:
        result.append(member_type(*item))
    return result


def member_type(age, handicap):
    return 'Senior' if age >= 55 and handicap > 7 else 'Open'


print(openOrSenior([[45, 12], [55, 21], [19, -2], [104, 20]]))  # ['Open', 'Senior', 'Open', 'Senior'])
print(openOrSenior([[16, 23], [73, 1], [56, 20], [1, -1]]))  # ['Open', 'Open', 'Senior', 'Open'])
