result = 0
day = 1
counter = 0
match = 0
points = 0
winners_list = []
numbers_list = []
file = open("day4_1_input.txt", "r")
input = file.read()
input_list = input.split('\n')
for line in input_list:
    input_list_a = line.split('|')
    for value in input_list_a:
        numbers = value.split(' ')
        for number in numbers:
            if number.isnumeric() == True and counter % 2 == 0:
                winners_list.append(number)
            elif number.isnumeric() == True and not counter % 2 == 0:
                numbers_list.append(number)
        counter += 1
        if counter%2 == 0:
            day += 1
        for i in winners_list:
            if i in numbers_list:
                match += 1
    if match > 1:
        result = 2 ** (match - 1)
    elif match == 1:
        result = 1
    else:
        result = 0
    points += result
    winners_list = []
    numbers_list = []
    match = 0
print(points)
