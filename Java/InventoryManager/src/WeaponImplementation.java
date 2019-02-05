import java.util.Scanner;

public class WeaponImplementation extends ItemImplementation implements Weapon {
    private int damage;

    public int getDamage() {
        return damage;
    }

    public void setDamage(int damage) {this.damage = damage;}

    public static Weapon copyOf(Weapon original) {
        Weapon weapon = new WeaponImplementation();
        ((WeaponImplementation) weapon).setDamage(original.getDamage());
        ((WeaponImplementation) weapon).setName(original.getName());
        ((WeaponImplementation) weapon).setGoldValue(original.getGoldValue());
        ((WeaponImplementation) weapon).setWeight(original.getWeight());
        return weapon;
    }

    public boolean parseDamageValue(String damageString){
        try {
            int newDamage = Integer.parseInt(damageString);
            if (newDamage < 0) {
                this.damage = 0;
            } else {
                this.damage = newDamage;
            }
        } catch (Exception e) {
            return false;
        }
        return true;
    }

    public static Weapon deserialize(Scanner scan) {
        Weapon weapon = new WeaponImplementation();
        ((WeaponImplementation) weapon).parseDamageValue(scan.next());
        ((WeaponImplementation) weapon).parseName(scan.next());
        ((WeaponImplementation) weapon).parseGoldValue(scan.next());
        ((WeaponImplementation) weapon).parseWeight(scan.next());
        return weapon;
    }

    public String toString() {
        String[] strings = {getName(), "" + getWeight(), "" + getGoldValue(),
                "" + String.format("%.4f", getValueWeightRatio()), "" + getDamage()};

        // Makes sure strings don't exceed character limit of 40, if they do takes substring, appends "..."
        for (int i = 0; i < strings.length; i++) {
            if (strings[i].length() > maxStringCharLimit) {
                strings[i] = strings[i].substring(0, maxStringCharLimit);
                strings[i] += "...";
            }
        }

        // Adds info to strings, (e.g. dmg, gp)
        String[] newStrings = {strings[0], strings[1] + " lbs", strings[2] + " GP", strings[3] + " ratio",
                strings[4] + " DMG"};

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
        return "Weapon |" + outputString;
    }
}
