// fort0142

public class BattleBoatsBoard {
    private int rowTotal;
    private int columnTotal;
    private  BattleCell[][] grid;
    private Boat[] battleShips;
    private int boatTotal;
    private boolean debugMode;

    public int maxRowIndex() {return rowTotal - 1;}

    public int maxColIndex() {return columnTotal - 1;}

    public int getBoatTotal() {return boatTotal;}

    public BattleCell[][] getGrid() {return grid;}


    public BattleBoatsBoard(int m_rows, int n_columns, boolean debugMode) { // Constructor for BattleBoatsBoard
        rowTotal = m_rows;
        columnTotal = n_columns;
        grid = new BattleCell[rowTotal][columnTotal];
        this.debugMode = debugMode;
        int rowLength = grid.length, colLength = grid[0].length;
        for (int i = 0; i < rowLength; i++) {
            for (int j = 0; j < colLength; j++) {
                grid[i][j] = new BattleCell(false, false, debugMode, false, false); // Initialize grid w/BattleCell obj.
            }
        }

        boatTotal = getTotalBoats(rowTotal, columnTotal);
        battleShips = new Boat[boatTotal];
        System.out.println("Total number of boats based on "
                + rowTotal + " rows and " + columnTotal + " columns is: " + boatTotal + "\n");

        int boatsToPlace = boatTotal;
        while (boatsToPlace > 0) {
            int randRow = (int) (Math.random() * (rowTotal));
            int randCol = (int) (Math.random() * (columnTotal));

            if (!grid[randRow][randCol].isBoat()) {
                int heading = (int) (Math.random() * (4)) + 1;
                int rowChange = 0, colChange = 0; // Used to change pos of row, col depending on heading

                if (heading == 1) {
                    rowChange = -2; // Moves two rows up in grid, "North"
                } else if (heading == 2) {
                    colChange = 2; // Moves two cols right in grid, "East"
                } else if (heading == 3) {
                    rowChange = 2; // Moves two rows down in grid, "South"
                } else if (heading == 4) {
                    colChange = -2; // Moves two cols left in grid, "West"
                }
                boolean boatAdded =
                        boatInitialization
                                (randRow, randCol, randRow + rowChange, randCol + colChange, heading, boatsToPlace);
                if (boatAdded) {
                    boatsToPlace -= 1;
                }
            }
        }
    }

    private boolean boatInitialization(int randRow, int randCol, int boatRow, int boatCol, int heading, int boatsToPlace) {
        int boatMiddleRow = 0, boatMiddleCol = 0; // Keeps track of grid locations to setBoat() later if tests pass.
        int boatEndRow = 0, boatEndCol = 0;

        boolean [] pass = new boolean[2]; // Keeps track of whether successive non-diagonal boat pieces can be placed

        int changeRow = 1, changeCol = 1; // Standard for headings 1 and 4, "north" and "west"
        if (heading == 2) // Decrement last boat col for heading 2, "east"
            changeCol = -1;
        if (heading == 3) // Decrement last boat row for heading 3, "south"
            changeRow = -1;

        // Works backwards to randomly picked row, col seeing if it can place a boat piece in each location
        for (int i = 0; boatRow != randRow || boatCol != randCol; boatRow += changeRow, boatCol += changeCol, i++){
            if (inGrid(boatRow, boatCol)) {
                if (grid[boatRow][boatCol].isBoat())
                    return false;
                pass[i] = true;
                if (i == 0) { // Stores values if tests successful for initialization
                    boatEndRow = boatRow;
                    boatEndCol = boatCol;
                } else {
                    boatMiddleRow = boatRow;
                    boatMiddleCol = boatCol;
                }
            }
            if (boatCol == randCol) // resets boatRow/boatCol for proper iteration to work for all four headings
                boatCol -= changeCol;
            if (boatRow == randRow) {
                boatRow -= changeRow;
            }
        }

        if (pass[0] && pass[1]) {
            int boatNumber = boatsToPlace - 1;
            battleShips[boatNumber] =
                    new Boat(randRow, randCol, boatMiddleRow, boatMiddleCol, boatEndRow, boatEndCol, grid, boatNumber);
            return true;
        }
        return false;
    }

    private static int getTotalBoats(int rowNumber, int colNumber) {
        if (rowNumber == 3 || colNumber == 3) {
            return 1;
        } else if ((rowNumber > 3 && rowNumber <= 5) || (colNumber > 3 && colNumber <= 5)) {
            return 2;
        } else if ((rowNumber > 5 && rowNumber <= 7) || (colNumber > 5 && colNumber <= 7)) {
            return 3;
        } else if ((rowNumber > 7 && rowNumber <= 9) || (colNumber > 7 && colNumber <= 9)) {
            return 4;
        } else {
            return 6;
        }
    }

    public void drawBoard() {
        System.out.println("Don't go alone. Use this key to help.");
        if (debugMode) {
            System.out.println("Debug Mode Activated.   __Debug_Boat__: means boat hidden from player.");
        }
        System.out.println("--Boat-Spotted: boat visible to player.   __Boat_Hit____: Boat, hit");
        System.out.println("____Water_____: water.       Spleesh___Miss: miss ");
        for (int i = 0; i <= rowTotal; i++) { // Iterates over grid to output board state to terminal
            for (int j = 0; j <= columnTotal; j++) {
                if (i == 0) {
                    if (j == 0) {
                        System.out.print("     ");
                    } else if (j % 2 != 0) { // Had an issue with centering top numbers, this is my "workaround."
                        System.out.print("       " + (j - 1) + "         ");
                    } else {
                        System.out.print("       " + (j - 1) + "       ");
                    }
                } else if (j == 0) {
                    System.out.print(String.format("%6d", i - 1));
                } else {
                    String drawing = grid[i - 1][ j - 1].getDrawing();
                    System.out.print(String.format("%6s", drawing));
                }
            }
            System.out.println();
        }
    }

    public boolean boatSunk(int row, int col) {
        /* Wanted to map row, col pairs to dictionary boat number in battleShips based on location in array
         * but can't import dictionary. Comparing two numbers is better than searching through all three row, col pairs
         * for each member of the array.
         */
        for (Boat boat: battleShips) {
            if (grid[row][col].getBoatNumber() == boat.getBoatNumber()) {
                return boat.isSunk(grid);
            }
        }
        return false;
    }

    public void droneAttack(int row, int col) {
        grid[row][col].setDroneSent();
        int [][] rowColChange = { {-1, -1}, {-1, 0}, {-1, 1},
                                  {0, -1}, {0, 0}, {0, 1},
                                  {1, -1}, {1, 0}, {1, 1}};
        for (int i = 0, length = rowColChange.length; i < length; i++) {
            int rowChange = rowColChange[i][0];
            int colChange = rowColChange[i][1];
            if (inGrid(row + rowChange, col + colChange))
                grid[row + rowChange][col + colChange].setRevealed();
        }
    }

    public boolean inGrid(int row, int col) {
        return (row >= 0 && row <= maxRowIndex() && col >= 0 && col <= maxColIndex());
    }
}
