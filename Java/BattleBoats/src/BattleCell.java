// fort0142

public class BattleCell {
    private boolean boat;
    private boolean hit;
    private boolean debug;
    private boolean droneSent;
    private boolean revealed;
    private int boatNumber = -1;

    public BattleCell(boolean boat, boolean hit, boolean debug, boolean droneSent, boolean revealed) {
        this.boat = boat;
        this.hit = hit;
        this.debug = debug;
        this.droneSent = droneSent;
        this.revealed = revealed;
    }

    public void setBoat() {boat = true;}

    public boolean isBoat() {return boat;}

    public void setHit() {hit = true;}

    public boolean isHit() {return hit;}

    public void setDroneSent() {droneSent = true;}

    public boolean droneAlreadySent() {return droneSent;}

    public void setRevealed() {revealed = true;} // Used for the drone in a specific area to see boat

    public void setBoatNumber(int number) {boatNumber = number;}

    public int getBoatNumber() {return boatNumber;}

    public String getDrawing() {
        if (boat && debug && !revealed && !hit) { // Only displays during debug mode and boat. To show hidden boats.
            return " __Debug_Boat__ ";
        } else if (boat && revealed && !hit) { // Boat, not hit and drone revealed it.
            return " --Boat-Spotted ";
        } else if (boat && hit) { // Boat and hit.
            return " __Boat_Hit____ ";
        } else if (hit) { // Hit and not boat is a miss/water "spleesh"
            return " Spleesh___Miss ";
        } else { // Water, open part of board.
            return " ____Water_____ ";
        }
    }
}






