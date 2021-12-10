import collections

def parseInput(filename):
    fish = []
    with open(filename) as file:
        line = file.readline()
        fish = [int(x) for x in line.split(',')]
    
    return fish

def parseInput2(filename):
    fish = [0] * 9
    with open(filename) as file:
        line = file.readline()
        numbers = [int(x) for x in line.split(',')]
        for i in range(9):
            fish[i] = numbers.count(i)
    return collections.deque(fish)


def day(fish):
    newFish = []
    for i in range(len(fish)):
        if fish[i] == 0:
            newFish.append(8)
            fish[i] = 6
        else:
            fish[i] -= 1
    
    if len(newFish) > 0:
        for nf in newFish:
            fish.append(nf)
    
    return fish

def day2(fish):
    #print(fish)
    zeros = fish[0]
    fish.rotate(-1)
    fish[8] = zeros
    fish[6] += zeros
    return fish

if __name__ == '__main__':
    fish = parseInput('testInput.txt')
    
    for i in range(80):
        #print(i, fish)
        fish = day(fish)

    print('part1', len(fish))

    #part2
    fish2 = parseInput2('input.txt')
    for i in range(256):
        fish2 = day2(fish2)
    part2 = 0
    for i in range(9):
        part2 += fish2[i]

    print('part2', part2)