numbers = []
for i in range(1,101):
    numbers.append(i)

for i in numbers:
    if i % 15 == 0:
        numbers[numbers.index(i)] = "fizzbuzz"
    elif i % 5 == 0:
        numbers[numbers.index(i)] = "buzz"
    elif i % 3 == 0:
        numbers[numbers.index(i)] = "fizz"

for i in numbers:
    print(i)

