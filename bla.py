"""
Calculate the area of patches of fertle land in a field
and list the areas from smallest to largest.
"""

import json
import sys

class BLA():

    def __init__(self, width, height):
        """
        Initialise the grid.

        In this grid:
        0 = Barren land
        1 = Fertile land
        2 = Fertile land whose area has been or is being calculated.
        """
        self.grid = self._makeGrid(width, height, 1)
        self.width = width
        self.height = height

    def _makeGrid(self, width, height, defaultVal = 0):
        """Create a grid of width by height and set all values to defaultVal"""

        grid = [[ defaultVal for dummy_col in xrange(width)] for dummy_row in xrange(height)]
        return grid

    def fillCellsInSquare(self, bottomLeft, topRight, value = 0):
        """
        Fill a square section of a grid with a given value

        Arguments:        
        bottomLeft -- bottomleft point of square
        topRight -- topRight point of square
        value -- the value to fill in the cells within the square
        """

        topLeft = (topRight[0], bottomLeft[1])
        bottomRight = (bottomLeft[0], topRight[1])

        for row in xrange(bottomRight[0], topRight[0] + 1):
            for col in xrange(topLeft[1], topRight[1] + 1):
                self.grid[row][col] = value

    def getNeighbors(self, cell):
        """
        Get the 4 neighbours of a cell; bottom, top, left and right
        """
        neighbors = []
        if cell[0] > 0:
            neighbors.append((cell[0] - 1, cell[1]))
        if cell[0] < self.height - 1:
            neighbors.append((cell[0] + 1, cell[1]))
        if cell[1] > 0:
            neighbors.append((cell[0], cell[1] - 1))
        if cell[1] < self.width - 1:
            neighbors.append((cell[0], cell[1] + 1))
        return neighbors

    def calcArea(self, cell):
        """
        Given a cell which represents a part of a patch of fertile land,
        use DFS to calculate the area of that patch of fertile land.

        NB: This function mutates the grid.
        After this function runs, all cells connected to {cell} become 0
        """
        
        # Use an array as the stack used for DFS.
        stack = []

        # Keep count of cells in the fertile land. Number of cells
        # in the patch are equal to the area.
        count = 0
        row = cell[0]
        col = cell[1]
        self.grid[row][col] = 0
        stack.append((row, col))

        # DFS magic :-)
        while len(stack) != 0:
            cell = stack.pop()
            count += 1
            neighbors = self.getNeighbors(cell)
            for neighborCell in neighbors:
                neighborRow = neighborCell[0]
                neighborCol = neighborCell[1]
                if self.grid[neighborRow][neighborCol] == 1:

                    # When a cell is visited set its value in the grid to 0 before
                    # adding it to stack so that it is not visited again.
                    self.grid[neighborRow][neighborCol] = 2
                    stack.append((neighborRow, neighborCol))

        return count

    def insertArea(self, area, results):
        """
        Insert the area of a patch of land into a list, results, which contains
        the areas of other patches of land in ascending order. List remains 
        sorted in ascending order after insertion.

        This way the list of areas is sorted in O(n pow 2) time as opposed to O((n pow 2) log(n))
        if the items were to be all added to the list then sorted.
        """
        
        # If list is empty then just insert area into list
        if len(results) == 0:
            results.append(area)
            return

        # If list already contains patch(es) of land then insert the area of 
        # the new patch at the index of the first element that is larger/equal
        # to it then shift that element and those after it to the right.
        for idx in xrange(len(results)):
            if results[idx] >= area:
                results.insert(idx, area)
                return

        # If no element is larger than the value of area then append area to
        # the end
        results.append(area)



    def calcFertileAreas(self):
        """
        Return a list that contains the areas of patches of land
        in a grid, sorted in ascending order.
        """
        results = []

        # Loop through all cells in the grid and if a cell is part of a patch of
        # fertile land then use DFS and calculate the area of the patch of fertile
        # land that cell belongs to.
        for row in xrange(self.height):
            for col in xrange(self.width):
                if self.grid[row][col] == 1:
                    area = self.calcArea((row, col))
                    self.insertArea(area, results)

        return results
                    


def prepInput(inputStr):
    """
    Convert input from string to suitable Python types.

    The string:
    {"48 192 351 207", "48 392 351 407"}

    Is converted to a a list of tuples:
    [((48, 192), (351, 207)), ((48, 392), (351, 407))]
    """

    # Replace the enclosing the braces with square brackets to convert the
    # string to a JSON array. This enables using the json module to parse the
    # string and return an array of strings.
    inputStr = inputStr.replace("{", "[")
    inputStr = inputStr.replace("}", "]")
    
    inputStrArr = json.JSONDecoder().decode(inputStr)

    barrenLands = []

    # Loop through the array of strings and convert the values to tuples
    # that cotain the ordered pair representing the coordinates.
    for item in inputStrArr:
        arr = item.split(" ")

        # Create the ordered pair to be of the form (y, x) (instead of (x,y) )
        # in order to fit the (row, col) model of the grid used in the BLA class
        bottomLeft = (int(arr[1]), int(arr[0]))
        topRight = (int(arr[3]), int(arr[2]))
        barrenLand = (bottomLeft, topRight)
        barrenLands.append(barrenLand)

    return barrenLands

def prepOuput(resultArr):
	"""
	Receives the result as an array containing the areas of the patches of fertile
	land sorted in ascending order and formats it as a string in the style of the
	expected output.

	If result is: [123, 456]
	returned string will be: "123 456" 
	"""
	resultStr = ""
	for item in resultArr:
		resultStr += str(item) + " "

	return resultStr + "\n"

# This section only runs when this module is excuted as a command in the shell
if __name__ == "__main__":


    input1 = sys.stdin.read()
    barrenLands = prepInput(input1)
    land = BLA(400, 600)

    for barrenLand in barrenLands:
        land.fillCellsInSquare(barrenLand[0], barrenLand[1], 0)

    output = land.calcFertileAreas()
    

    sys.stdout.write(prepOuput(output))