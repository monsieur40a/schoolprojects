import java.util.Scanner;

public class ItemImplementation implements Item{
    public static final int maxStringCharLimit = 40;
    private String name;
    private int goldValue;
    private double weight;

    public String getName() {
        if (name == null)
            name = "Unnamed item of truth.";
        return name;
    }

    public void setName(String name) {this.name = name;}

    public int getGoldValue() {
        return goldValue;
    }

    public void setGoldValue(int goldValue) {this.goldValue = goldValue;}

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {this.weight = weight;}

    public double getValueWeightRatio() {
        return goldValue/weight;
    }

    public static Item copyOf(Item original) {
        Item item = new ItemImplementation();
        ((ItemImplementation) item).setName(original.getName());
        ((ItemImplementation) item).setGoldValue(original.getGoldValue());
        ((ItemImplementation) item).setWeight(original.getWeight());
        return item;
    }

    public boolean parseName(String nameString) {
        if (nameString == null) {
            name = "Unnamed item of truth.";
            return true;
        }
        this.name = nameString;
        return true;
    }

    public boolean parseGoldValue(String goldValueString){
        try {
            int newGoldValue = Integer.parseInt(goldValueString);
            if (newGoldValue < 0) {
                this.goldValue = 0;
            } else {
                this.goldValue = newGoldValue;
            }
        } catch (Exception e) {
            return false;
        }
        return true;
    }

    public boolean parseWeight(String weightString){
        try {
            double newWeight = Double.parseDouble(weightString);
            if (newWeight < 0) {
                this.weight = 0;
            } else {
                this.weight = newWeight;
            }
        } catch (Exception e) {
            return false;
        }
        return true;
    }

    public static Item deserialize(Scanner scan) {
        Item item = new ItemImplementation();
        ((ItemImplementation) item).parseName(scan.next());
        ((ItemImplementation) item).parseGoldValue(scan.next());
        ((ItemImplementation) item).parseWeight(scan.next());
        return item;
    }

    public String toString() {
        String[] strings = {getName(), "" + getWeight(), "" + getGoldValue(), "" + String.format("%.4f", getValueWeightRatio())};

        // Makes sure strings don't exceed character limit of 40, if they do takes substring, appends "..."
        for (int i = 0; i < strings.length; i++) {
            if (strings[i].length() > maxStringCharLimit) {
                strings[i] = strings[i].substring(0, maxStringCharLimit);
                strings[i] += "...";
            }
        }

        // Adds info to strings, (e.g. dmg, gp)
        String[] newStrings = {strings[0], strings[1] + " lbs", strings[2] + " GP", strings[3] + " ratio"};

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
        return  "Item   |" + outputString;
    }
}
