
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
    for i in range(len(array)): #wszystkie
        if i >= 0 and i+2 < len(array):
            nextSum = array[i] + array[i+1] + array[i+2]
            if prevSum and prevSum < nextSum:
                count+=1
            prevSum = nextSum
        print(prevSum, nextSum, count)
        


if __name__ == '__main__':
    input1 = parseInput('input1.txt')
    input2 = parseInput('input2.txt')
    print(part2(input2))

