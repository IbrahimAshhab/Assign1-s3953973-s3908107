from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell
from spreadsheet.doublyLinkedList import DoublyLinkedList


# class ListNode:
#     '''
#     Define a node in the linked list
#     '''
#
#     def __init__(self, word_frequency: WordFrequency):
#         self.word_frequency = word_frequency
#         self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.spread_sheet = DoublyLinkedList()
        self.num_rows = 0
        self.num_cols = 0
        # TO BE IMPLEMENTED
        pass

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
            self.spread_sheet.insert_end(DoublyLinkedList())

        currentRow = self.spread_sheet.head
        row = 0
        while currentRow != None:
            for col in range(self.num_cols):
                currentRow.data.insert_end(Cell(row, col, None))
            currentRow = currentRow.next
            row += 1

        for cell in lCells:
            currentRow = self.spread_sheet.head
            while currentRow != None:
                currentCol = currentRow.data.head
                while currentCol != None:
                    if currentCol.data.row == cell.row and currentCol.data.col == cell.col:
                        currentCol.data = cell
                    currentCol = currentCol.next

                currentRow = currentRow.next
        pass

    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """
        self.num_rows += 1  # this might cause an issue might not but most likely not
        self.spread_sheet.insert_end(DoublyLinkedList())
        tail = self.spread_sheet.head
        while tail.next != None:
            tail = tail.next
        for col in range(self.num_cols):
            tail.data.insert_end(
                Cell(self.num_rows-1, col, None))

        return True

    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        currentRow = self.spread_sheet.head
        row = 0
        while currentRow != None:
            currentRow.data.insert_end(
                Cell(row, self.num_cols, None))
            currentRow = currentRow.next
            row += 1

        self.num_cols += 1
        return True

    def insertRow(self, rowIndex: int) -> bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.   If inserting as first row, specify rowIndex to be 0.   If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True

    def insertCol(self, colIndex: int) -> bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """

        # TO BE IMPLEMENTED
        pass

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
        cellUpdated = False

        currentRow = self.spread_sheet.head
        while currentRow != None:
            currentCol = currentRow.data.head
            while currentCol != None:
                if currentCol.data.row == rowIndex and currentCol.data.col == colIndex:
                    currentCol.data.val = value
                    cellUpdated = True
                currentCol = currentCol.next
            currentRow = currentRow.next

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return cellUpdated

    def rowNum(self) -> int:
        """
        @return Number of rows the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        # pass
        if self.spread_sheet.head is None:
            return 0
        numRows = 1
        currentCell = self.spread_sheet.head

        while currentCell.next != None:
            currentCell = currentCell.next
            numRows += 1
        # TO BE IMPLEMENTED
        return numRows

    def colNum(self) -> int:
        """
        @return Number of column the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        # pass
        if self.spread_sheet.head is None:
            return 0

        numCols = 1
        currentCell = self.spread_sheet.head.data.head

        while currentCell.next != None:
            currentCell = currentCell.next
            numCols += 1

        # TO BE IMPLEMENTED
        return numCols

    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
            """
        value_list = []
        currentRow = self.spread_sheet.head
        while currentRow != None:
            currentCol = currentRow.data.head
            while currentCol != None:
                if currentCol.data.val == value:
                    value_list.append(
                        (currentCol.data.row, currentCol.data.col))
                currentCol = currentCol.next
            currentRow = currentRow.next

        return value_list

    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        non_none_cells = []
        currentRow = self.spread_sheet.head
        while currentRow != None:
            currentCol = currentRow.data.head
            while currentCol != None:
                if currentCol.data.val != None:
                    non_none_cells.append(currentCol.data)
                currentCol = currentCol.next
            currentRow = currentRow.next

        return non_none_cells
