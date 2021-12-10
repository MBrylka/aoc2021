from PIL import Image

class Vent:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1

        self.x2 = x2
        self.y2 = y2

        self.diagonal = True

        if x1 == x2 or y1 == y2:
            self.diagonal = False
            
    
    def getMaxX(self):
        return self.x1 if self.x1 > self.x2 else self.x2
        
    def getMaxY(self):
        return self.y1 if self.y1 > self.y2 else self.y2

    def write(self):
        print([self.x1, self.y1], [self.x2, self.y2], self.diagonal)


def parseInput(filename):
    vents = []
    with open(filename) as file:
        lines = file.readlines()

        for line in lines:
            line = line.replace('-> ', ' ')
            coords = [x.strip() for x in line.split(' ') if x]
            #print(coords)
            p1 = [int(x) for x in coords[0].split(',')]
            p2 = [int(x) for x in coords[1].split(',')]
            #print(p1, p2)
            vents.append(Vent(p1[0], p1[1], p2[0], p2[1]))
    return vents

def createMap(width, height):
    map = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append('.')
        map.append(row)
    return map

def printMap(Map, width, height):
    for i in range(height):
        for j in range(width):
            print(Map[i][j], end="")
        print()

def applyVents(map, vent, maxX, maxY):
    x1 = vent.x1
    x2 = vent.x2
    y1 = vent.y1
    y2 = vent.y2

    if not vent.diagonal:
        
        for i in range(min(y1, y2), max(y1, y2)+1):
            for j in range(min(x1, x2), max(x1, x2)+1):
                if map[i][j] == '.':
                    map[i][j] = '1'
                else:
                    map[i][j] = str(int(map[i][j])+1)
    else:
        #diagonal
        print(vent.x1, vent.y1, vent.x2, vent.y2)
        movex = 1 if x1 < x2 else -1
        movey = 1 if y1 < y2 else -1
        
        for i in range(abs(x2-x1)+1):
            if map[y1][x1] == '.':
                map[y1][x1] = '1'                
            else:
                map[y1][x1] = str(int(map[y1][x1])+1)
            x1 += movex
            y1 += movey

    return map

def countIntersections(Map, maxX, maxY):
    sum = 0
    for i in range(maxY):
        for j in range(maxX):
            if Map[i][j] not in ['.', '1']:
                sum += 1
    return sum

if __name__ == '__main__':
    vents = parseInput('input.txt')
    maxX = 0
    maxY = 0
    for vent in vents:
        #vent.write()
        if vent.getMaxX() > maxX:
            maxX = vent.getMaxX()
        
        if vent.getMaxY() > maxY:
            maxY = vent.getMaxY()
    maxX += 1
    maxY += 1

    Map = createMap(maxX, maxY)
    #printMap(Map, maxX, maxY)

    for vent in vents:
        Map = applyVents(Map, vent, maxX, maxY)
    print()
    #printMap(Map, maxX, maxY)

im= Image.new('RGB', (maxX, maxY))
for i in range(maxY):
    for j in range(maxX):
        if Map[i][j] == '.':
            im.putpixel( (j, i), (255, 255, 255, 255) )
        elif Map[i][j] == '1':
            im.putpixel( (j, i), (0, 0, 0, 255) )
        else:
            im.putpixel( (j, i), (255, 0, 0, 255) )
im.save('test.png')

print(countIntersections(Map, maxX, maxY))
    