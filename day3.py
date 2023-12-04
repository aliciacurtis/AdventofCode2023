with open("day3.txt", "r") as my_file:
    engine, grand_total, gears, total_ratio = [], 0, {}, 0
    for x in my_file:
        this_row = []
        for y in x[0:len(x)]:
            this_row.append(y)
        engine.append(this_row)

    row_num = -1
    for row in engine:
        row_num += 1
        current_number, current_gear, part_number = '', '', False
        for q in range(len(row)):
            if row[q].isdigit():
                current_number += row[q]
                if row_num > 0:
                    low, high = max(q - 1, 0), min(q + 1, len(row) - 2)
                    for x in range(low, high + 1):
                        if engine[row_num - 1][x] != '.' and not engine[row_num - 1][x].isdigit():
                            part_number = True
                            if engine[row_num - 1][x] == '*':
                                current_gear = (row_num - 1, x)
                                if current_gear not in gears:
                                    gears[(row_num - 1, x)] = 0
                for y in range(q - 1, q + 2, 2):
                    if not part_number and y >= 0 and engine[row_num][y] != '.' and not engine[row_num][y].isdigit():
                        part_number = True
                        if engine[row_num][y] == '*':
                            current_gear = (row_num, y)
                            if current_gear not in gears:
                                gears[(row_num, y)] = 0
                if not part_number and row_num + 1 < len(engine):
                    low, high = max(q - 1, 0), min(q + 1, len(row) - 2)
                    for z in range(low, high + 1):
                        if engine[row_num + 1][z] != '.' and not engine[row_num + 1][z].isdigit():
                            part_number = True
                            if engine[row_num + 1][z] == '*':
                                current_gear = (row_num + 1, z)
                                if current_gear not in gears:
                                    gears[(row_num + 1, z)] = 0

            elif part_number and current_number:
                grand_total += int(current_number)
                if current_gear in gears:
                    if gears[current_gear] > 0:
                        ratio = int(current_number) * gears[current_gear]
                        total_ratio += ratio
                    else:
                        gears[current_gear] = int(current_number)
                part_number, current_number, current_gear = False, '', ''

            else:
                current_number = ''

print(grand_total)
print(total_ratio)
