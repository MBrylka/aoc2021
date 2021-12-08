import copy

class BingoNum:
    def __init__(self, val, mark):
        self.value = val
        self.marked = mark

    def markNumber(self, val):
        if self.value == val:
            self.marked = True

    def write(self):
        print('\t', self.value, self.marked, end=" ")


class Board:
    def __init__(self):
        self.matrix = []

    def addLine(self, line):
        records = [int(x) for x in line.split(' ') if x]
        row = []
        for i in range(5):
            row.append(BingoNum(records[i], False))
        self.matrix.append(row)

    def checkNumber(self, num):
        for i in range(5):
            for j in range(5):
                self.matrix[i][j].markNumber(num)
                win = self.isWinning(i, j)
                if win:
                    #print win and return True
                    sum = self.getUncheckedSum()
                    print(num, sum, num*sum, 'WIN')
                    return True
        
        return False
    
    def getUncheckedSum(self):
        sum = 0
        for i in range(5):
            for j in range(5):
                if not self.matrix[i][j].marked:
                    sum += self.matrix[i][j].value
        return sum

    def isWinning(self, row, col):
        winning = True
        for i in range(5):
            if not self.matrix[row][i].marked:
                winning = False
        
        if winning:
            return True
        
        winning = True

        for i in range(5):
            if not self.matrix[i][col].marked:
                winning = False
        if winning:
            return True

        return False

    def write(self):
        for row in range(5):
            for col in range(5):
                self.matrix[row][col].write()
            print()


def parseInput(filename):
    with open(filename) as file:
        lines = file.readlines()
        win_numberLine = lines[0]
        win_numbers = [int(x) for x in win_numberLine.strip().split(',')]

        boards = []
        for i in range(1, len(lines), 6):
            board = Board()
            for j in range(i + 1, i + 6):
                board.addLine(lines[j].strip())
            boards.append(copy.deepcopy(board))

    return win_numbers, boards


def part1(numbers, boards):
    found = False
    for num in numbers:
        for board in boards:
            found = board.checkNumber(num)
            board.write()
            print('---------------------------------------')
            if found:
                break
        if found:
            break

def part2(numbers, boards):
    for num in numbers:
        print(num, '####################################')
        boardsToRemove = []
        for board in boards:
            found = board.checkNumber(num)
            board.write()
            print('-----------')
            if found:
                boardsToRemove.append(board)
        for toRemove in boardsToRemove:
            boards.remove(toRemove)



if __name__ == '__main__':
    win_numbers, boards = parseInput("input1.txt")
    part2(win_numbers, boards)

    


