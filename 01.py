def main():
    with open('01.txt') as file:
        lines = file.read().splitlines()
        calories =[]
        totalCurrentCalories = 0
        for line in lines:
            if line:
                totalCurrentCalories = totalCurrentCalories + int(line)
            else:
                calories.append(totalCurrentCalories)
                totalCurrentCalories = 0

    print('Part One:'+str(max(calories)))
    # START OF PART TWO#
    calories = sorted(calories)
    calories.reverse()
    sumOfTopThree= calories[0]+ calories[1]+calories[2]
    print('Part Two: '+str(sumOfTopThree))




if __name__ == '__main__':
    main()

