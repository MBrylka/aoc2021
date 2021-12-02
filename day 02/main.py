
def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.strip().split() for line in lines]
    return lines

def processCommands(array):
    position = 0
    aim = 0
    depth = 0
    for command in array:
        value = int(command[1])
        
        if command[0] == 'forward':
            position += value
            depth += value * aim
        if command[0] == 'up':
            aim -= value
        if command[0] == 'down':
            aim += value

    return (position * aim, position * depth)


if __name__ == '__main__':
    input = parseInput('input1.txt')
    multi = processCommands(input)
    print(multi[0]) # part1
    print(multi[1]) # part2