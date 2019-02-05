// fort0142

public class Boat {
    private int bowRow;
    private int bowCol;
    private int amidshipRow;
    private int amidshipCol;
    private int sternRow;
    private int sternCol;
    private int boatNumber;

    // Initializes boat (bow, amidship, stern) and boatnumber in grid and here.
    public Boat(int frontRow, int frontCol, int midRow, int midCol, int backRow, int backCol,
                      BattleCell[][] grid, int boatNumber) {
        bowRow = frontRow;
        bowCol = frontCol;
        amidshipRow = midRow;
        amidshipCol = midCol;
        sternRow = backRow;
        sternCol = backCol;
        this.boatNumber = boatNumber;

        grid[bowRow][bowCol].setBoat();
        grid[amidshipRow][amidshipCol].setBoat();
        grid[sternRow][sternCol].setBoat();
        grid[bowRow][bowCol].setBoatNumber(boatNumber);
        grid[amidshipRow][amidshipCol].setBoatNumber(boatNumber);
        grid[sternRow][sternCol].setBoatNumber(boatNumber);
    }

    public int getBoatNumber() {return boatNumber;}

    public boolean isSunk(BattleCell[][] grid) {
        return grid[bowRow][bowCol].isHit() && grid[amidshipRow][amidshipCol].isHit() && grid[sternRow][sternCol].isHit();
    }
}
