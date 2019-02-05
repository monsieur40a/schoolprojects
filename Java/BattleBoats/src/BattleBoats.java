// fort0142

import java.util.Scanner;

public class BattleBoats {
    private static final int minimumWidth = 3;
    private static final int minimumHeight = 3;
    private static final int maximumWidth = 12;
    private static final int maximumHeight = 12;
    private Scanner scan = new Scanner(System.in);

    public BattleBoatsBoard initializeBoard() {
        int width = 0, height = 0;
        boolean debugMode = false, invalidDimensions = true;

        while (invalidDimensions) {
            System.out.println("Enter a height for the board between 3 and 12, inclusive.");
            height = scan.nextInt();
            System.out.println("Enter a width for the board between 3 and 12, inclusive.");
            width = scan.nextInt();
            if (width < minimumWidth || width > maximumWidth || height < minimumHeight || height > maximumHeight) {
                System.out.println("Invalid dimensions entered. Try again.");
            } else {
                invalidDimensions = false;
            }
        }
        System.out.println("\nDimensions adequate.\nPlay in debug mode? Y/N");
        String debug = scan.next().toLowerCase();
        if (debug.equals("y") || debug.equals("yes") ) {
            debugMode = true;
            System.out.println("Debug Mode Enabled.\n");
        } else {
            System.out.println("Debug Mode Disabled.\n");
        }
        return new BattleBoatsBoard(height, width, debugMode);
    }

    public void startGamePlay(BattleBoatsBoard board) {
        int turnNumber = 1, totalShots = 0;
        int boatTotal = board.getBoatTotal();
        int row = -1, col = -1;
        boolean penalty, droneSent, inputSuccess;
        BattleCell[][] grid = board.getGrid();

        System.out.println("Are you ready to play BattleBoats!? The boat battling game of epicness!\n");

        while (boatTotal > 0) {
            penalty = droneSent = inputSuccess = false;

            try {
                board.drawBoard();

                System.out.println
                        ("Turn Number: " + turnNumber + " Boats Remaining: " + boatTotal + " Total shots: " + totalShots);
                System.out.print("Input a row, col to target(e.g. 0 0): ");
                scan = new Scanner(System.in); // Needed otherwise infinite loop if try fails
                row = scan.nextInt();
                col = scan.nextInt();
                System.out.println("\nSend a drone to this location? Enter y/n. y - to send drone. n - to attack.");
                String drone = scan.next().toLowerCase();

                if (drone.equals("y") || drone.equals("yes")) {
                    droneSent = true;
                    System.out.println("\nRecon. Takes four turns. Sending drone to " + row + " , " + col);
                }
                inputSuccess = true;
            } catch (Exception e) {
                e.printStackTrace();
                System.out.println("Ya done goofed, try to enter input correctly, turns + 1.\n\n");
            }
            if (inputSuccess) {
                if (board.inGrid(row, col)) {
                    if ((grid[row][col].isHit() && !droneSent) || (grid[row][col].droneAlreadySent() && droneSent)) {
                        penalty = true;
                        System.out.println("\nPenalty. One turn lost. Location already chosen.");
                    } else if (droneSent) {
                        board.droneAttack(row, col);
                    } else if (grid[row][col].isBoat()) {
                        grid[row][col].setHit();
                        if (board.boatSunk(row, col)) {
                            System.out.println("\nSunk. Success!");
                            boatTotal -= 1;
                        } else {
                            System.out.println("\nHit. Success!");
                        }
                    } else {
                        grid[row][col].setHit();
                        System.out.println("\nMiss. Oh noes. Try to guess better.");
                    }
                } else { // penalty if out of bounds/grid
                    penalty = true;
                    System.out.println("\nPenalty. One turn lost. Location(s) entered is out of bounds.");
                }
                if (boatTotal != 0) { // Don't want to increase turns if last turn/game over
                    if (penalty)
                        turnNumber += 1; // skip 1 turn for penalty
                    if (droneSent)
                        turnNumber += 4; // skip 4 turns for sending drone
                    turnNumber += 1;
                }
                if (!droneSent) {
                    totalShots += 1; // Everything counts as a cannon shot except when drone sent
                }
            } else {
                turnNumber += 1;
                continue;
            }

            System.out.println();
        }
        board.drawBoard();
        System.out.println("You Win! Total turns was " + turnNumber + " Total shots: " + totalShots);
    }
}
