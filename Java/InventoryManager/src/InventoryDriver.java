// Initiates a loop where the user can manage their inventory
// May also design and implement whatever additional classes and methods needed
    // to support this driver so long as you implement every part of the description below

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Iterator;
import java.util.Scanner;

public class InventoryDriver {
    private CharacterImplementation character = new CharacterImplementation();
    private static final Scanner scan = new Scanner(System.in);


    public static void main(String[] args) {
        InventoryDriver driver = new InventoryDriver();
        System.out.println("=====================================");
        System.out.println("RPG Inventory Manager! Plan Your Fate!");
        boolean prompt = true;
        while (prompt) {
            driver.printOptions();
            prompt = driver.processOption(driver.getOption());
        }
        System.out.println("This concludes RPG Inventory Manager.");

    }

    public void printOptions() {
        System.out.println("=====================================");
        System.out.println("Select an option:");
        System.out.println("0: Print Inventory");
        System.out.println("1: Add Unequippable Item");
        System.out.println("2: Add Armor");
        System.out.println("3: Add Weapon");
        System.out.println("4: Optimize Inventory");
        System.out.println("5: Optimize Equipment");
        System.out.println("6: Quit");
        System.out.println("7: Add Items from File");
        System.out.println("8: Add Armor from File");
        System.out.println("9: Add Weapons from File");
        System.out.println("=====================================");
    }

    public String inputError() {
        return "Looks like you entered something incorrectly. Try again.";
    }

    public int getOption() {
        boolean successful = false;
        int option = -1;
        while (!successful) {
            try {
//                Scanner scan = new Scanner(System.in);
                String entry = scan.nextLine();
                option = Integer.parseInt(entry);
                for (int validInt : new int[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}) {
                    if (option == validInt)
                        successful = true;
                }
                if (!successful) {
                    printOptions();
                    System.out.println("Invalid Number, try again.");
                }
            } catch (Exception e) {
                printOptions();
                System.out.println(inputError());
            }
        }
        return option;
    }

    public boolean processOption(int option) {
        switch (option) {
            case 0:
                printInventory();
                break;
            case 1:
                addUnequippableItem();
                break;
            case 2:
                addArmor();
                break;
            case 3:
                addWeapon();
                break;
            case 4:
                optimizeInventory();
                break;
            case 5:
                optimizeEquipment();
                break;
            case 7:
                addItemsFromFile();
                break;
            case 8:
                addArmorFromFile();
                break;
            case 9:
                addWeaponsFromFile();
                break;
            default:
                return false; // Set prompt to false for "Quit"
        }
        return true; // Set prompt to true for continued management of inventory
    }

    public void printInventory() {
        Armor[] armorSet = character.getArmorSet();
        Weapon myWeapon = character.getEquippedWeapon();
        boolean printTotalWeight = false, printEquipment = false;
        // Goes through inventory and outputs armor/item/weapon
        Iterator<Item> iterator = character.inventory();
        if (iterator.hasNext()) {
            System.out.println("Current Inventory\n");
            printTotalWeight = true;
        }
        while (iterator.hasNext()) {
            Item item = iterator.next();
            System.out.println(item);
        }

        if (myWeapon != null) {
            printEquipment = true;
            printTotalWeight = true;
        }
        for (int i = 0; i < armorSet.length; i++) {
            if (armorSet[i] != null) {
                printEquipment = true;
                printTotalWeight = true;
                i = armorSet.length;
            }
        }

        if (printEquipment) {
            System.out.println();
            System.out.println("Equipped Weapons and Armor:");
            if (myWeapon != null) {
                System.out.println(myWeapon);
                System.out.println();
            }
            for (Armor a: armorSet) {
                if (a != null) {
                    System.out.println(a);
                }
            }
            System.out.println();
            System.out.println("Total Equipped Weight (Weapon, Armor Only): " + character.totalEquippedWeight());
            System.out.println();
        }
        if (printTotalWeight) {
            System.out.println();
            System.out.println("Total Weight of Everything: " + character.getTotalWeight());
            System.out.println();
        }
    }

    public void addUnequippableItem() {
        boolean nameSetSuccess = false, weightSetSuccess = false, goldSetSuccess = false;
        ItemImplementation item = new ItemImplementation();
        while (!nameSetSuccess) {
            System.out.print("Enter item name: ");
            nameSetSuccess = item.parseName(scan.nextLine());
            if (!nameSetSuccess) {
                System.out.println("Invalid Format. Only alphanumeric and ' allowed.");
            }
        }
        while (!weightSetSuccess) {
            System.out.print("Enter item weight: ");
            weightSetSuccess = item.parseWeight(scan.nextLine());
            if (!weightSetSuccess) {
                System.out.println("Invalid Format. Only doubles allowed.");
            }
        }
        while (!goldSetSuccess) {
            System.out.print("Enter item value: ");
            goldSetSuccess = item.parseGoldValue(scan.nextLine());
            if (!goldSetSuccess) {
                System.out.println("Invalid Format. Only integers allowed.");
            }
        }
        character.addItem(item);
    }

    public void addArmor() {
        boolean nameSetSuccess = false, weightSetSuccess = false, goldSetSuccess = false;
        boolean slotSetSuccess = false, ratingSetSuccess = false;
        Armor armor = new ArmorImplementation();
        while (!slotSetSuccess) {
            System.out.println("Enter armor slot: 0=chest, 1=legs, 2=hands, 3=feet, 4=helmet, 5=shield");
            slotSetSuccess = ((ArmorImplementation) armor).parseSlotValue(scan.nextLine());
            if (!slotSetSuccess) {
                System.out.println("Invalid Format. Only integers allowed.");
            }
        }
        while (!nameSetSuccess) {
            System.out.print("Enter armor name: ");
            nameSetSuccess = ((ArmorImplementation) armor).parseName(scan.nextLine());
            if (!nameSetSuccess) {
                System.out.println("Invalid Format. Only alphanumeric and ' allowed.");
            }
        }
        while (!ratingSetSuccess) {
            System.out.print("Enter armor rating: ");
            ratingSetSuccess = ((ArmorImplementation) armor).parseRatingValue(scan.nextLine());
            if (!ratingSetSuccess) {
                System.out.println("Invalid Format. Only integers allowed.");
            }
        }
        while (!weightSetSuccess) {
            System.out.print("Enter armor weight: ");
            weightSetSuccess = ((ArmorImplementation) armor).parseWeight(scan.nextLine());
            if (!weightSetSuccess) {
                System.out.println("Invalid Format. Only doubles allowed.");
            }
        }
        while (!goldSetSuccess) {
            System.out.print("Enter armor value: ");
            goldSetSuccess = ((ArmorImplementation) armor).parseGoldValue(scan.nextLine());
            if (!goldSetSuccess) {
                System.out.println("Invalid Format. Only integers allowed.");
            }
        }
        character.addItem(armor);
    }

    public void addWeapon() {
        boolean nameSetSuccess = false, weightSetSuccess = false, goldSetSuccess = false;
        boolean damageSetSuccess = false;
        Weapon weapon = new WeaponImplementation();
        while (!nameSetSuccess) {
            System.out.print("Enter weapon name: ");
            nameSetSuccess = ((WeaponImplementation) weapon).parseName(scan.nextLine());
            if (!nameSetSuccess) {
                System.out.println("Invalid Format. Only alphanumeric and ' allowed.");
            }
        }
        while (!damageSetSuccess) {
            System.out.print("Enter weapon damage: ");
            damageSetSuccess = ((WeaponImplementation) weapon).parseDamageValue(scan.nextLine());
            if (!damageSetSuccess) {
                System.out.println("Invalid Format. Only integers allowed.");
            }
        }
        while (!weightSetSuccess) {
            System.out.print("Enter weapon weight: ");
            weightSetSuccess = ((WeaponImplementation) weapon).parseWeight(scan.nextLine());
            if (!weightSetSuccess) {
                System.out.println("Invalid Format. Only doubles allowed.");
            }
        }
        while (!goldSetSuccess) {
            System.out.print("Enter weapon value: ");
            goldSetSuccess = ((WeaponImplementation) weapon).parseGoldValue(scan.nextLine());
            if (!goldSetSuccess) {
                System.out.println("Invalid Format. Only integers allowed.");
            }
        }
        character.addItem(weapon);
    }

    public void optimizeInventory() {
        boolean unoptimized = true;
        while (unoptimized) {
            System.out.print("Enter target carry weight: ");
            String stringWeight = scan.nextLine();
            try {
                double weight = Double.parseDouble(stringWeight);
                character.optimizeInventory(weight);
                ArrayList<Item> droppedItems = character.getDroppedItems();
                if (droppedItems.size() != 0)
                    System.out.println("Dropped items:");
                for (Item item : droppedItems) {
                    System.out.println(item);
                }
                unoptimized = false;
                droppedItems.clear();
            } catch (Exception e) {
                System.out.println(inputError());
            }
        }
    }

    public void optimizeEquipment() {
        System.out.println("Inventory and Items prior to Optimization: \n\n");
        printInventory();
        character.optimizeEquipment();
        System.out.println("Inventory and Items after Equipment Optimization: \n\n");
        printInventory();
    }

    public void addItemsFromFile() {
//        System.out.print("Enter a filename to create items from: ");
        try (Scanner scanFromFile = new Scanner(new File("Item Templates.txt"))) {
            while (scanFromFile.hasNext()) {
                Item item = ItemImplementation.deserialize(scanFromFile);
                character.addItem(item);
            }
        } catch (FileNotFoundException e) {
            System.out.println("Invalid file name. Try again.");
        }
    }

    public void addArmorFromFile() {
//        System.out.print("Enter a filename to create items from: ");
        try (Scanner scanFromFile = new Scanner(new File("Armor Templates.txt"))) {
            while (scanFromFile.hasNext()) {
                Armor armor = ArmorImplementation.deserialize(scanFromFile);
                character.addItem(armor);
            }
        } catch (FileNotFoundException e) {
            System.out.println("Invalid file name. Try again.");
        }
    }

    public void addWeaponsFromFile() {
//        System.out.print("Enter a filename to create items from: ");
        try (Scanner scanFromFile = new Scanner(new File("Weapon Templates.txt"))) {
            while (scanFromFile.hasNext()) {
                Weapon weapon = WeaponImplementation.deserialize(scanFromFile);
                character.addItem(weapon);
            }
        } catch (FileNotFoundException e) {
            System.out.println("Invalid file name. Try again.");
        }
    }





}
