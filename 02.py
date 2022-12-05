def main():
    with open('02.txt') as file:
        lines = file.read().splitlines()
        games = [(letters[0], letters[2]) for letters in lines]
        score = 0
        for round in games:
            if round[0] == 'A':
                if round[1] == 'X':
                    score += 4
                elif round[1] == 'Y':
                    score += 8
                else:
                    score += 3
            elif round[0] == 'B':
                if round[1] == 'X':
                    score += 1
                elif round[1] == 'Y':
                    score += 5
                else:
                    score += 9
            else:
                if round[1] == 'X':
                    score += 7
                elif round[1] == 'Y':
                    score += 2
                else:
                    score += 6
        print('Part One:'+str(score))
        score = 0
        for round in games:
            if round[0] == 'A':
                if round[1] == 'X':
                    score += 3
                elif round[1] == 'Y':
                    score += 4
                else:
                    score += 8
            elif round[0] == 'B':
                if round[1] == 'X':
                    score += 1
                elif round[1] == 'Y':
                    score += 5
                else:
                    score += 9
            else:
                if round[1] == 'X':
                    score += 2
                elif round[1] == 'Y':
                    score += 6
                else:
                    score += 7
        print('Part Two: ' + str(score))









if __name__ == '__main__':
    main()

