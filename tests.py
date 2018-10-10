import bla, unittest


class TestBla(unittest.TestCase):
	def testPrepInput(self):
		"""Test for prepInput"""

		inputStr = '{"0 292 399 307"}'

		expected = [((292, 0), (307, 399))]
		
		self.assertEqual(bla.prepInput(inputStr), expected)


	def testBLAMakeGrid(self):
		"""Test for BLA._makeGrid"""
		width = 400
		height = 600

		land = bla.BLA(width, height)

		gridHeight = len(land.grid)
		gridWidth = len(land.grid[0])

		self.assertEqual(gridHeight, height)
		self.assertEqual(gridWidth, width)

	def testBLAFillCellsInSquare(self):
		"""Test for BLA.fillCellsInSquare"""
		
		def getGridMaxVal(grid):
			"""Return max value in a Grid"""
			maxVal = 0
			for row in grid:
				maxVal = max(maxVal, max(row))

			return maxVal

		width = 400
		height = 600
		bottomLeft = (35, 0)
		topRight = (63, 77)

		land = bla.BLA(width, height)

		# Since by default the grid is initialised with 1's the max value in
		# the grid should be 1
		maxVal = getGridMaxVal(land.grid)
		self.assertEqual(maxVal, 1)

		# Fill a section of the grid with 5's. After that the max value in the 
		# grid should now be 5
		land.fillCellsInSquare(bottomLeft, topRight, 5)
		maxVal = getGridMaxVal(land.grid)
		self.assertEqual(maxVal, 5)

		# Also make sure all cells in the section are now filled with 5's
		for row in xrange(bottomLeft[0], topRight[0] + 1):
			for col in xrange(bottomLeft[1], topRight[1] + 1):
				 self.assertEqual(land.grid[row][col], 5)

	def testBLAInsertArea(self):
		"""Test for BLA.insertArea"""

		width = 10
		height = 14
		land = bla.BLA(width, height)

		# Start with an empty list then insert values and make sure the list
		# stays sorted in ascending order as values are inserted
		items = []
		area = 35
		land.insertArea(area, items)
		expected = [35]
		self.assertEqual(items, expected)

		area = 21
		land.insertArea(area, items)
		expected = [21, 35]
		self.assertEqual(items, expected)

		area = 56
		land.insertArea(area, items)
		expected = [21, 35, 56]
		self.assertEqual(items, expected)

	def testBLAGetNeighbors(self):
		"""Test for BLA.getNeighbours"""
		width = 10
	 	height = 14
	 	land = bla.BLA(width, height)

	 	# First element in grid should have just 2 neighbors. Top and right.
	 	neighbors = land.getNeighbors((0,0))
	 	expected = [(0,1),(1,0)]
	 	neighbors.sort()
	 	expected.sort()
	 	self.assertEqual(neighbors, expected)

	 	neighbors = land.getNeighbors((5,5))
	 	expected = [(4,5), (6,5), (5, 4), (5, 6)]
	 	neighbors.sort()
	 	expected.sort()
	 	self.assertEqual(neighbors, expected)

	def testBLACalcArea(self):
		"""Test for BLA.calcArea"""
		width = 5
		height = 5
		land = bla.BLA(width, height)

		area = land.calcArea((0,0))
		expectedArea = 25
		self.assertEqual(area, expectedArea)