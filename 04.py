def main():
    with open("04.txt") as puzzleInput:
        lines = puzzleInput.read().splitlines()
    rangePairs = parseRangePairs(lines)
    numberOfOverlappingRangePairs = 0
    for rangePair in rangePairs:
        if rangePair[0].isContainedIn(rangePair[1]) or rangePair[1].isContainedIn(rangePair[0]):
            numberOfOverlappingRangePairs += 1
    print('Part One:' + str(numberOfOverlappingRangePairs))
    numberOfOverlappingRangePairs = 0
    for rangePair in rangePairs:
        if rangePair[0].isOverlappingWith(rangePair[1]) or  rangePair[1].isOverlappingWith(rangePair[0]) :
            numberOfOverlappingRangePairs += 1
    print('Part Two:' + str(numberOfOverlappingRangePairs))


def parseRangePairs(lines):
    rangePairs = []
    for line in lines:
        rangeStrings = line.split(',')
        firstRange = parseRange(rangeStrings[0])
        secondRange = parseRange(rangeStrings[1])
        rangePairs.append((firstRange, secondRange))
    return rangePairs


def parseRange(rangeString):
    startAndEnd = rangeString.split('-')
    return Range(int(startAndEnd[0]), int(startAndEnd[1]))


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        if start > end:
            raise NameError('start is bigger than end!')

    def __str__(self):
        return str(self.start) + '-' + str(self.end)

    def isContainedIn(self, otherRange):
        return self.start >= otherRange.start and self.end <= otherRange.end
    def isOverlappingWith(self,otherRange):
        return self.start in range(otherRange.start,otherRange.end+1) or self.end in range(otherRange.start,otherRange.end+1)



if __name__ == '__main__':
    main()
