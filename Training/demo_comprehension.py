

numbers = [12,43,67,89,43,67,43,56,23]

print(numbers)



tientallen = {number: number//10 for number in numbers if number > 50}

print(tientallen)

tientallen = {}
for number in numbers:
    if number > 50:
        tientallen[number] = number//10

print(tientallen)

tientallen = (number//10 for number in numbers if number > 50)
print(tientallen)


def times_100(numbers):
    return (number * 100 for number in numbers)

def times_100(numbers):
    for number in numbers:
        yield number * 100




for n in times_100([1,2,3,4,5,6,7,8,9]):
    print(n)