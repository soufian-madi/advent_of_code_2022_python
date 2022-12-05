def main():
    with open('03.txt') as file:
        lines = file.read().splitlines()
        rucksacks = [getCompartments(line) for line in lines]
        score = 0
        for rucksack in rucksacks:
            print(rucksack)
            for letter in rucksack[0]:
                if letter in rucksack[1]:
                    if ord(letter) > 90:
                        print(letter)
                        print(ord(letter) - 96)
                        score += (ord(letter) - 96)
                    else:
                        print(letter)
                        print(ord(letter) - 38)
                        score += (ord(letter) - 38)
                    break
            print('\n')
        print('Part One:' + str(score))
        i = 0
        score = 0
        while i < len(lines):
            print((lines[i], lines[i + 1], lines[i + 2]))
            for letter in lines[i]:
                if letter in lines[i + 1] and letter in lines[i + 2]:
                    print('the badge is ' + letter * 10 + '\n')
                    if ord(letter) > 90:
                        score += (ord(letter) - 96)
                    else:
                        score += (ord(letter) - 38)
                    break
            i += 3
        print('Part Two:' + str(score))


def getCompartments(line):
    length = len(line)
    return (line[:length // 2], line[length // 2:])


if __name__ == '__main__':
    main()
