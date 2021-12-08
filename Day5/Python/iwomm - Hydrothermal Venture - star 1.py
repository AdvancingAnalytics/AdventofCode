class Vent:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        
    @property
    def x1(self):
        return self.__x1

    @property
    def x2(self):
        return self.__x2

    @property
    def y1(self):
        return self.__y1

    @property
    def y2(self):
        return self.__y2
    
    def findVentLocations(self):
        x = self.x1
        y = self.y1
        
        #ensure line is not diagonal
        if (self.x1 == self.x2) or (self.y1 == self.y2):
                yield x, y

        # iterate over range between point '(x,y)' to point '(x2, y2)' regardless of direction of the line
        while x != self.x2 or y != self.y2:
            if x < self.x2:
                x += 1
            elif x > self.x2:
                x -= 1
            if y < self.y2:
                y += 1
            elif y > self.y2:
                y -= 1
                
            # each (x,y) on the line is a vent which will be returned by this function to be added to the map
            #ensure line is not diagonal
            if (self.x1 == self.x2) or (self.y1 == self.y2):
                yield x, y
            
        
    def coordinates(line : str):
        lineSplit = line.split(" -> ")
        lineStart = lineSplit[0].split(",")
        lineEnd = lineSplit[1].split(",")
        
        return Vent(int(lineStart[0]), int(lineStart[1]), int(lineEnd[0]), int(lineEnd[1]))

class VentMap:

    def __init__(self):
        #initialise empty dict of vent locations
        self.__locations = {}
        #initialise count for dangerous locations (more than one vent line passes through point on the map)
        self.__dangerousLocationsCount = 0
    
    def addVent(self, vent):
        for x, y in vent.findVentLocations():
            self.add(x, y)
    
    def add(self, x, y):
        #for each vent location (x,y) either add to or increment ventMap
        if not x in self.__locations.keys():
            self.__locations[x] = {}
        
        if not y in self.__locations[x].keys():
            self.__locations[x][y] = 0
            
        self.__locations[x][y] += 1
        
        # increment only when vent hits dangerous threshold otherwise will double increment
        if self.__locations[x][y] == 2:
            self.__dangerousLocationsCount += 1
                
    @property
    def locations(self):
        return self.__locations

    @property
    def dangerousLocationsCount(self):
        return self.__dangerousLocationsCount

inputData = open('input.txt', 'r')

lines = inputData.readlines()

ventMap = VentMap()

for line in lines:
    vent = Vent.coordinates(line)
    ventMap.addVent(vent)

print('# vent line intersections: ', ventMap.dangerousLocationsCount)
