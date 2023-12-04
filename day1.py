with open("day1.txt", "r") as my_file:
    running_sum = 0
    for line in my_file:
        this_sum = ''
        for x in line:
            if x.isdigit():
                this_sum += x
                break
        for x in range(len(line) - 1, -1, -1):
            if line[x].isdigit():
                this_sum += line[x]
                break
        running_sum += int(this_sum)
    print(running_sum)

with open("day1.txt", "r") as my_file:
    running_sum = 0
    for line in my_file:
        this_sum, numbers = '', []
        for x in range(len(line)):
            if line[x:x + 3] == 'one':
                numbers.append([x, 1, 3])
            elif line[x:x + 3] == 'two':
                numbers.append([x, 2, 3])
            elif line[x:x + 5] == 'three':
                numbers.append([x, 3, 5])
            elif line[x:x + 4] == 'four':
                numbers.append([x, 4, 4])
            elif line[x:x + 4] == 'five':
                numbers.append([x, 5, 4])
            elif line[x:x + 3] == 'six':
                numbers.append([x, 6, 3])
            elif line[x:x + 5] == 'seven':
                numbers.append([x, 7, 5])
            elif line[x:x + 5] == 'eight':
                numbers.append([x, 8, 5])
            elif line[x:x + 4] == 'nine':
                numbers.append([x, 9, 4])

        if len(numbers) >= 1:
            numbers = [numbers[0], numbers[len(numbers) - 1]]
            for x in range(0, numbers[0][0]):
                if line[x].isdigit():
                    this_sum += line[x]
                    break
            if not this_sum:
                this_sum += str(numbers[0][1])

            if len(numbers) > 1:
                for x in range(len(line) - 1, numbers[1][0] + numbers[1][2] - 1, -1):
                    if line[x].isdigit():
                        this_sum += line[x]
                        break
                if len(this_sum) == 1:
                    this_sum += str(numbers[1][1])

            else:
                for y in range(len(line) - 1, numbers[0][0] + numbers[0][2] - 1, -1):
                    if line[y].isdigit():
                        this_sum += line[y]
                        break
                if len(this_sum) == 1:
                    this_sum += str(numbers[0][1])

        else:
            for x in line:
                if x.isdigit():
                    this_sum += x
                    break
            for x in range(len(line) - 1, -1, -1):
                if line[x].isdigit():
                    this_sum += line[x]
                    break

        running_sum += int(this_sum)

    print(running_sum)
