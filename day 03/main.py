
def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def part1(input1):
    inputLen = len(input1)
    dict = {}

    for line in input1:
        for i in range(len(line)):
            val = int(line[i])
            if i in dict.keys():
                dict[i] += val
            else:
                dict[i] = val
    gamma = ""
    for key in dict:
        if dict[key] >= inputLen/2:
            gamma += "1"
        else:
            gamma += "0"
    
    epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])
    print("gamma", gamma)
    print("epsilon", epsilon)

    return int(gamma,2)*int(epsilon,2)

def filter(array, position, bit):
    retVal = []
    for element in array:
        if element[position] == bit:
            retVal.append(element)
    return retVal

def getoxygen(input1):
    recordLen = len(input1[0])
    for i in range(recordLen):
        bit = 0
        inputLen = len(input1)
        if(inputLen > 1):
            for j in range(inputLen):
                record = input1[j]
                if record[i] == '1':
                    bit+=1
            if bit >= inputLen/2:
                input1 = filter(input1, i, '1')
            else:
                input1 = filter(input1, i, '0')

    return input1

def getCo2(input1):
    recordLen = len(input1[0])
    for i in range(recordLen):
        bit = 0
        inputLen = len(input1)
        if(inputLen > 1):
            for j in range(inputLen):
                record = input1[j]
                
                if record[i] == '1':
                    bit+=1
            if bit < inputLen/2:
                input1 = filter(input1, i, '1')
            else:
                input1 = filter(input1, i, '0')

    return input1




def part2(input1):
    ox= getoxygen(input1)
    co2 = getCo2(input1)
    print(ox, co2)
    return int(ox[0],2)*int(co2[0],2)


if __name__ == '__main__':
    input1 = parseInput("input1.txt")

    print(part1(input1))
    print(part2(input1))