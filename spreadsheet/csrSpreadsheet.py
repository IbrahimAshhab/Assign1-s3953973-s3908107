from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------


class CSRSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.ColA = []
        self.ValA = []
        self.SumA = []

    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        lCellsCopy = lCells.copy()

        numIters = len(lCells)
        for x in range(numIters):
            lowest_cell = lCells[0]
            for i in range(len(lCells)):
                if lCells[i].row == lowest_cell.row:
                    if lCells[i].col < lowest_cell.col:
                        lowest_cell = lCells[i]
                if lCells[i].row < lowest_cell.row:
                    lowest_cell = lCells[i]
            self.ColA.append(lowest_cell.col)
            self.ValA.append(lowest_cell.val)
            lCells.remove(lowest_cell)

        num_rows = 0

        for cell in lCellsCopy:
            if cell.row > num_rows - 1:
                num_rows = cell.row + 1

        cumulativeSum = 0
        for x in range(num_rows):
            for cell in lCellsCopy:
                if cell.row == x:
                    cumulativeSum += cell.val
            self.SumA.append(cumulativeSum)
        pass

    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        self.SumA.append(self.SumA[-1])
        return True
        # TO BE IMPLEMENTED

    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        return True
        # TO BE IMPLEMENTED

    def insertRow(self, rowIndex: int) -> bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        if (rowIndex < 0) or (rowIndex >= self.rowNum()):
            return False
        # REPLACE WITH APPROPRIATE RETURN VALUE
        self.SumA.insert(rowIndex, self.SumA[rowIndex])
        return True

    def insertCol(self, colIndex: int) -> bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        if colIndex < 0 or colIndex >= self.colNum():
            return False

        for i in range(0, len(self.ColA)):
            if self.ColA[i] >= colIndex:
                self.ColA[i] += 1
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        # should update be able to update an empty cell

        # TO BE IMPLEMENTED
        if (rowIndex < 0) or (rowIndex >= len(self.SumA) - 1):
            return False

        if colIndex < 0 or colIndex >= max(self.ColA) + 1:
            return False
        # REPLACE WITH APPROPRIATE RETURN VALUE

        current_row = 0
        sum = 0

        # looping thru all values, incrementing sum
        for i in range(len(self.ColA)):
            while sum == self.SumA[current_row + 1]:
                current_row += 1
            sum += self.ValA[i]
            if current_row == rowIndex and self.ColA[i] == colIndex:
                difference = value - self.ValA[i]
                self.ValA[i] = value
                for j in range(current_row + 1, len(self.SumA)):
                    self.SumA[j] += difference
                return True
        return False

    def rowNum(self) -> int:
        """
        @return Number of rows the spreadsheet has.
        """
        # TO BE IMPLEMENTED

        return len(self.SumA) - 1

    def colNum(self) -> int:
        """
        @return Number of column the spreadsheet has.
        """
        # TO BE IMPLEMENTED
        return max(self.ColA) + 1

    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
            """

        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        result = []
        current_row = 0
        sum = 0
        for i in range(len(self.ColA)):
            while sum == self.SumA[current_row + 1]:
                current_row += 1
            sum += self.ValA[i]
            if self.ValA[i] == value:
                result.append((current_row, self.ColA[i]))

        return result

    def entries(self) -> [Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """
        result = []
        current_row = 0
        sum = 0
        for i in range(len(self.ColA)):
            while sum == self.SumA[current_row + 1]:
                current_row += 1
            sum += self.ValA[i]
            result.append(Cell(current_row, self.ColA[i], self.ValA[i]))

        return result
