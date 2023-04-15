import math
from typing import List

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
        self.num_cols = 0

    def buildSpreadsheet(self, lCells: List[Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        # Slower to do sort and build in two steps, but easier
        cells = sorted(lCells, key=lambda c: (c.row, c.col))
        cumsum = 0
        previousRow = -1
        for cell in cells:
            for i in range(previousRow, cell.row):
                self.SumA.append(cumsum)
            previousRow = cell.row
            self.ColA.append(cell.col)
            self.num_cols = max(self.num_cols, cell.col)
            self.ValA.append(cell.val)
            cumsum += cell.val
        self.SumA.append(cumsum)

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
        self.num_cols += 1
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
        if not (0 <= colIndex < self.num_cols):
            return False
        self.num_cols += 1
        for i, col in enumerate(self.ColA):
            if col >= colIndex:
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

        # TO BE IMPLEMENTED
        if not (0 <= rowIndex < self.rowNum()):
            return False

        if not (0 <= colIndex < self.colNum()):
            return False
        # REPLACE WITH APPROPRIATE RETURN VALUE

        # looping thru all values, incrementing sum

        for i, c in enumerate(self.entries()):
            if c.row == rowIndex and c.col == colIndex:
                difference = value - self.ValA[i]
                self.ValA[i] = value
                for j in range(c.row + 1, len(self.SumA)):
                    self.SumA[j] += difference
                return True

        # Can't update an existing cell so need to insert a new one
        # This is slow

        current_row = 0
        current_col = 0
        sum = 0
        # Find row
        while current_row != rowIndex and current_col < len(self.ColA):
            while sum == self.SumA[current_row + 1]:
                current_row += 1
                if current_row == rowIndex:
                    break
            else:
                sum += self.ValA[current_col]
                current_col += 1
        current_row = rowIndex
        # Find column
        found_index = len(self.ColA)
        for i in range(current_col, len(self.ColA)):
            # Check if reached end of the row or found a column that is before the new one
            if sum == self.SumA[current_row + 1]:
                found_index = i
                break
            elif self.ColA[i] < colIndex:
                found_index = i + 1
            sum += self.ValA[current_col]

        self.ColA.insert(found_index, colIndex)
        self.ValA.insert(found_index, value)

        for i in range(current_row + 1, len(self.SumA)):
            self.SumA[i] += value
        return True

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
        return self.num_cols + 1

    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
            """
        return [(c.row, c.col) for c in self.entries() if c.val == value]

    def entries(self) -> List[Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """
        result = []
        current_row = 0
        sum = 0
        for i in range(len(self.ColA)):
            while math.isclose(sum, self.SumA[current_row + 1]):
                current_row += 1
            sum += self.ValA[i]
            result.append(Cell(current_row, self.ColA[i], self.ValA[i]))

        return result
