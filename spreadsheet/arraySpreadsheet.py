from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.spread_sheet = []
        self.num_rows = 0
        self.num_cols = 0
        # TO BE IMPLEMENTED
        # pass

    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        for cell in lCells:
            if cell.row > self.num_rows:
                self.num_rows = cell.row + 1

            if cell.col > self.num_cols:
                self.num_cols = cell.col + 1

        for row in range(self.num_rows):
            self.spread_sheet.append([])
            for col in range(self.num_cols):
                self.spread_sheet[row].append(Cell(row, col, None))

        for cell in lCells:
            self.spread_sheet[cell.row][cell.col] = cell

        # TO BE IMPLEMENTED
        # pass

    def appendRow(self) -> bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        self.spread_sheet.append([])
        self.num_rows += 1

        for col in range(self.num_cols):
            self.spread_sheet[self.num_rows -
                              1].append(Cell(self.num_rows - 1, col, None))

        # TO BE IMPLEMENTED
        # pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True

    def appendCol(self) -> bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        self.num_cols += 1

        for row in range(self.num_rows):
            self.spread_sheet[row].append(Cell(row, self.num_cols - 1, None))

        # TO BE IMPLEMENTED
        # pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True

    def insertRow(self, rowIndex: int) -> bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  
        If inserting as first row, specify rowIndex to be 0.  
        If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.

        COMMENTS ARE FUCKED
        """
        if (rowIndex < -1) or (rowIndex >= self.num_rows):
            return False

        self.spread_sheet.insert(rowIndex+1, [])
        self.num_rows += 1

        for col in range(self.num_cols):
            self.spread_sheet[rowIndex+1].append(Cell(rowIndex + 1, col, None))

        # for loop updates values of rows and cols of cells in spreadsheet
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.spread_sheet[row][col].row = row
                self.spread_sheet[row][col].col = col
            # TO BE IMPLEMENTED
            # pass

            # REPLACE WITH APPROPRIATE RETURN VALUE
        return True

    def insertCol(self, colIndex: int) -> bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.
        If inserting as first column, specify colIndex to be 0.
        If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        if (colIndex < -1) or (colIndex >= self.num_cols):
            return False

        for row in range(self.num_rows):
            self.spread_sheet[row].insert(
                colIndex+1, Cell(row, colIndex + 1, None))

        self.num_cols += 1

        # for loop updates values of rows and cols of cells in spreadsheet
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.spread_sheet[row][col].row = row
                self.spread_sheet[row][col].col = col
        # TO BE IMPLEMENTED
        # pass

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
        if (rowIndex >= self.num_rows) or (rowIndex < 0) or (colIndex >= self.num_cols) or (colIndex < 0):
            return False

        self.spread_sheet[rowIndex][colIndex].val = value

        # TO BE IMPLEMENTED
        # pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True

    def rowNum(self) -> int:
        """
        @return Number of rows the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        # pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return len(self.spread_sheet)

    def colNum(self) -> int:
        """
        @return Number of column the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        # pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        if (len(self.spread_sheet) == 0):
            return 0
        else:
            return len(self.spread_sheet[0])

    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
        """
        value_list = []

        for row in range(len(self.spread_sheet)):
            for col in range(len(self.spread_sheet[row])):
                if self.spread_sheet[row][col].val == value:
                    value_list.append((row+1, col+1))

        # TO BE IMPLEMENTED
        # pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return value_list

    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        non_none_cells = []

        for row in range(len(self.spread_sheet)):
            for col in range(len(self.spread_sheet[row])):
                if (self.spread_sheet[row][col].val != None):
                    non_none_cells.append(self.spread_sheet[row][col])
        # TO BE IMPLEMENTED
        # pass

        # TO BE IMPLEMENTED
        return non_none_cells
