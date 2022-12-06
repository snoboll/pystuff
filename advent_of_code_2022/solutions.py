
def get_lines():
    with open('advent_of_code_2022/data.txt') as file:
        return [line for line in file]

def one():
    lines = get_lines()
    ans = 0
    current = 0
    elves = []
    for line in lines:
        if line != "\n":
            current += int(line)
        else:
            elves.append(current)
            current = 0
    print(sum(sorted(elves)[-3:]))

def two():
    lines = get_lines()
    score = 0
    for line in lines:
        opp = line.split()[0]
        outcome = line.split()[1]
        # lose
        if outcome == "X":
            if opp == "A":
                score += 3
            elif opp == "B":
                score += 1
            else:
                score += 2
        # draw
        elif outcome == "Y":
            score += 3
            if opp == "A":
                score += 1
            elif opp == "B":
                score += 2
            else:
                score += 3
        # win
        elif outcome == "Z":
            score += 6
            if opp == "A":
                score += 2
            elif opp == "B":
                score += 3
            else:
                score += 1

    print(score)

def three():
    import string

    lines = get_lines()
    ans = 0
    for line in lines:
        a = line[0:len(line) - 1]
        b = line[1:len(line)]
        # print(a,b)
        for char in a:
            if char in b:
                # print(char)
                ans += string.ascii_lowercase.index(char)
                break

    # print(lines)
    print(ord("L"))
    # print(ans)

three()