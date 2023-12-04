with (open("day2.txt", "r") as my_file):
    total_games, total_power = 0, 0
    for line in my_file:
        game_id = int(line[line.index('e') + 2:line.index(':')])
        punctuate = line.index(':')
        red, highest_red, blue, highest_blue, green, highest_green = 0, 0, 0, 0, 0, 0

        for x in range(punctuate + 2, len(line)):
            if line[x] == ';':
                punctuate = x
                highest_red, highest_blue, highest_green = max(red, highest_red), max(blue, highest_blue), max(green, highest_green)
                red, blue, green = 0, 0, 0
            elif line[x] == ',':
                punctuate = x
            elif line[x:x + 3] == 'red':
                red += int(line[punctuate + 2:x])
            elif line[x:x + 5] == 'green':
                green += int(line[punctuate + 2:x])
            elif line[x:x + 4] == 'blue':
                blue += int(line[punctuate + 2:x])

        highest_red, highest_blue, highest_green = max(red, highest_red), max(blue, highest_blue), max(green, highest_green)

        if highest_red <= 12 and highest_green <= 13 and highest_blue <= 14:
            total_games += game_id
        power = highest_red * highest_blue * highest_green
        total_power += power

    print(total_games)
    print(total_power)
