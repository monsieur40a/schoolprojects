import java.util.Scanner;

public class ArmorImplementation extends ItemImplementation implements Armor {
    private int slot;
    private int rating;

    public int getSlot() {
        return slot;
    }

    public void setSlot(int slot) {this.slot = slot;}

    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {this.rating = rating;}

    public static Armor copyOf(Armor original) {
        Armor armor = new ArmorImplementation();
        ((ArmorImplementation) armor).setSlot(original.getSlot());
        ((ArmorImplementation) armor).setRating(original.getRating());
        ((ArmorImplementation) armor).setName(original.getName());
        ((ArmorImplementation) armor).setGoldValue(original.getGoldValue());
        ((ArmorImplementation) armor).setWeight(original.getWeight());
        return armor;
    }

    public boolean parseSlotValue(String slotString) {
        try {
            int newSlot = Integer.parseInt(slotString);
            if (newSlot == 0 || newSlot == 1
                    || newSlot == 2 || newSlot == 3
                    || newSlot == 4 || newSlot == 5) {
                this.slot = newSlot;
            } else {
                this.slot = 0;
            }
        } catch (Exception e) {
            return false;
        }
        return true;
    }

    public boolean parseRatingValue(String ratingString) {
        try {
            int newRating = Integer.parseInt(ratingString);
            if (newRating < 0) {
                this.rating = 0;
            } else {
                this.rating = newRating;
            }
        } catch (Exception e) {
            return false;
        }
        return true;
    }

    public static Armor deserialize(Scanner scan) {
        Armor armor = new ArmorImplementation();
        ((ArmorImplementation) armor).parseSlotValue(scan.next());
        ((ArmorImplementation) armor).parseRatingValue(scan.next());
        ((ArmorImplementation) armor).parseName(scan.next());
        ((ArmorImplementation) armor).parseGoldValue(scan.next());
        ((ArmorImplementation) armor).parseWeight(scan.next());
        return armor;
    }

    public String toString() {
        String[] strings = {getName(), "" + getWeight(), "" + getGoldValue(),
                "" + String.format("%.4f", getValueWeightRatio()),  "" + getRating(), "" + getSlot()};

        // Makes sure strings don't exceed character limit of 40, if they do takes substring, appends "..."
        for (int i = 0; i < strings.length; i++) {
            if (strings[i].length() > maxStringCharLimit) {
                strings[i] = strings[i].substring(0, maxStringCharLimit);
                strings[i] += "...";
            }
        }

        int slot = getSlot();
        String armorType = "";
        switch (slot) {
            case 0:
                armorType += "/Chest";
                break;
            case 1:
                armorType += "/Legs";
                break;
            case 2:
                armorType += "/Hands";
                break;
            case 3:
                armorType += "/Feet";
                break;
            case 4:
                armorType += "/Head";
                break;
            default:
                armorType += "/Shield";
        }

        // Adds info to strings, (e.g. dmg, gp)
        String[] newStrings = {strings[0], strings[1] + " lbs", strings[2] + " GP",
                strings[3] + " ratio", strings[4] + " AR", strings[5] + armorType};

        // Determines maximum length for equal column spacing, standard spacing of 30
        int maximumLength = 30;
        for (int i = 0; i < newStrings.length; i++) {
            if (newStrings[i].length() > maximumLength) {
                maximumLength = newStrings[i].length();
            }
        }

        String outputString = "";
        for (String s : newStrings) {
            int spaces = maximumLength - s.length();
            outputString += s;
            for (int i = 0; i < spaces; i++) {
                outputString += " ";
            }
            outputString += "|";
        }
        return "Armor  |" + outputString;
    }
}
