
def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [int(line.strip()) for line in lines]
    return lines

def part1(array):
    count = 0
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            count += 1
    return count

def part2(array):
    count = 0
    prevSum = None
    for i in range(len(array)):
        if i+2 < len(array):
            nextSum = sum(array[x] for x in range(i, i+3))
            if prevSum and prevSum < nextSum:
                count+=1
            prevSum = nextSum
    return count
        

if __name__ == '__main__':
    input = parseInput('input1.txt')
    print(part1(input))
    print(part2(input))

