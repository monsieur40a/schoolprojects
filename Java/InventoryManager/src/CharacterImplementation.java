import java.util.Comparator;
import java.util.Iterator;

public class CharacterImplementation implements Character {
    private Weapon myWeapon;
    private Armor[] armorSet = new Armor[6];
    private ArrayList<Item> myInventory = new ArrayList<Item>(5);
    private ArrayList<Item> droppedItems = new ArrayList<Item>(5);
    private Map<String, Integer> abilityToScoreMap = new HashMap<String, Integer>(10);
    private Map<String, String> skillToAbilityMap = new HashMap<String, String>(10);
    private Map<String, Integer> skillToRankMap = new HashMap<String, Integer>(10);
    private Random rand = new Random(7919, 65537, 102611);

    public Map<String, Integer> getAbilityToScoreMap() {
        return abilityToScoreMap;
    }

    public Map<String, String> getSkillToAbilityMap() {
        return skillToAbilityMap;
    }

    public Map<String, Integer> getSkillToRankMap() {
        return skillToRankMap;
    }

    public int getAbilityScore(String abilityName) {
        if (abilityName == null) {
            throw new NullPointerException();
        }
        Integer score = abilityToScoreMap.get(abilityName);
        if (score == null) {
            return 10;
        }
        return score;
    }

    public void setAbilityScore(String abilityName, int abilityScore) {
        if (abilityName == null) {
            throw new NullPointerException();
        }
        if (abilityScore < 0) {
            throw new IllegalArgumentException();
        }
        abilityToScoreMap.put(abilityName, abilityScore);
    }

    public int getAbilityModifier(String abilityName) {
        if (abilityName == null) {
            throw new NullPointerException();
        }
        return getAbilityScore(abilityName) / 2 - 5;
    }

    public boolean checkAbility(String abilityName, int difficulty) {
        if (abilityName == null) {
            throw new NullPointerException();
        }
        if (difficulty < 0) {
            throw new IllegalArgumentException();
        }
        int randomInt = rand.randomInteger(1, 20);
        randomInt += getAbilityModifier(abilityName);
        if (randomInt >= difficulty) {
            return true;
        }
        return false;
    }

    public void addSkill(String skillName, String relatedAbility , int skillRanks) {
        if (skillName == null || relatedAbility == null) {
            throw new NullPointerException();
        }
        if (skillRanks < 0) {
            throw new IllegalArgumentException();
        }
        skillToAbilityMap.put(skillName, relatedAbility);
        skillToRankMap.put(skillName, skillRanks);
    }

    public int getSkillRanks(String skillName) {
        if (skillName == null) {
            throw new NullPointerException();
        }
        Integer skillRank = skillToRankMap.get(skillName);
        if (skillRank == null) {
            return 0;
        }
        return skillRank;
    }

    public void setSkillRanks(String skillName, int skillRanks) {
        if (skillName == null) {
            throw new NullPointerException();
        }
        if (skillRanks < 0) {
            throw new IllegalArgumentException();
        }
        Integer skillRank = skillToRankMap.get(skillName);
        if (skillRank == null) {
            throw new IllegalArgumentException();
        }
        skillToRankMap.put(skillName, skillRanks);
    }

    public String getRelatedAbility(String skillName) {
        if (skillName == null) {
            throw new NullPointerException();
        }
        String relatedAbility = skillToAbilityMap.get(skillName);
        if (relatedAbility == null) {
            throw new IllegalArgumentException();
        }
        return relatedAbility;
    }

    public int getSkillModifier(String skillName) {
        if (skillName == null) {
            throw new NullPointerException();
        }
        if (skillToRankMap.get(skillName) == null) {
            return 0;
        }
        return getSkillRanks(skillName) + getAbilityModifier(getRelatedAbility(skillName));
    }

    public boolean checkSkill(String skillName, int difficulty) {
        if (skillName == null) {
            throw new NullPointerException();
        }
        if (difficulty < 0) {
            throw new IllegalArgumentException();
        }
        int randomInt = rand.randomInteger(1, 20);
        randomInt += getSkillModifier(skillName);
        if (randomInt >= difficulty) {
            return true;
        }
        return false;
    }

    // Returns current set of armor, all pieces.
    public Armor[] getArmorSet() {
        return armorSet;
    }

    // Returns dropped items to print them elsewhere to show what was dropped from inventory optimization method.
    public ArrayList<Item> getDroppedItems() {
        return droppedItems;
    }

    // Creates iterator for list, sorts before returning iterator
    public Iterator<Item> inventory() {
        sortInventory();
        return myInventory.listIterator();
    }

    // Sorts in descending order by ValueWeightRatio using ItemComparator
    public void sortInventory() {
        myInventory.sort(new ItemComparator());
    }

    // Implements Linear Search on ArrayList, turns index if found, -1 if not found, has option to remove idx
    public int searchInventory(Item item, boolean remove) {
        // not sure if I need to return an index here
        Iterator<Item> iterator = inventory();
        int i = -1;
        while (iterator.hasNext()) {
            Item currentItem = iterator.next();
            i++;
            if (currentItem == item) {
                if (remove)
                    iterator.remove();
                return i;
            }
        }
        return -1;
    }

    // Adds copy of the itemTemplate to the inventory, converts as needed depending on type
    public void addItem(Item itemTemplate) {
        if (itemTemplate == null) {
            throw new NullPointerException();
        } else if (itemTemplate instanceof Weapon) {
            myInventory.add(WeaponImplementation.copyOf((Weapon)itemTemplate));
        } else if (itemTemplate instanceof Armor) {
            myInventory.add(ArmorImplementation.copyOf((Armor)itemTemplate));
        } else {
            myInventory.add(ItemImplementation.copyOf(itemTemplate));
        }
    }

    // Drops a specific item in the inventory, makes sure item is in inventory prior to drop
    public void dropItem(Item item) {
        if (item == null) {
            throw new NullPointerException();
        }
        int index = searchInventory(item, true);
        if (index == -1) {
            throw new ItemNotFoundException();
        } else {
            // Adds item to a list to be displayed as output to show item removed.
            // Dropped Items list cleared in order methods, could add in recovery option too.
            droppedItems.add(item);
        }
    }

    // Gets total weight of all items regardless of equipped or not
    public double getTotalWeight() {
        double totalWeight = 0.0;
        Iterator<Item> iterator = inventory();
        // Gets total weight from inventory
        while (iterator.hasNext()) {
            Item item = iterator.next();
            totalWeight += item.getWeight();
        }
        // Gets total weight from equipped weapon/armor
        totalWeight += totalEquippedWeight();
        return totalWeight;
    }

    // Returns only the total weight of the currently equipped items
    public double totalEquippedWeight() {
        double totalWeight = 0.0;
        if (myWeapon != null)
            totalWeight += myWeapon.getWeight();
        for (Armor armor: armorSet) {
            if (armor != null)
                totalWeight += armor.getWeight();
        }
        return totalWeight;
    }

    // Gets total armor rating for currently equipped armor
    public int getTotalArmorRating() {
        int totalRating = 0;
        for (Armor armor: armorSet) {
            if (armor != null)
                totalRating += armor.getRating();
        }
        return totalRating;
    }

    // Returns currently equipped weapon, including possibly null
    public Weapon getEquippedWeapon() {
        return myWeapon;
    }

    // Utilizing armorSet array returns current armor in slot, including possibly null
    public Armor getEquippedArmor(int slot) {
        switch (slot) {
            case 0:
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
                return armorSet[slot];
            default:
                throw new IllegalArgumentException();
        }
    }

    public void equipArmor(Armor armor) {
        // Unequips all armor if null
        if (armor == null) {
            for (int i = 0; i < armorSet.length; i++) {
                unequipArmor(i);
            }
        } else {
            // Searches inventory, only equips if found in myInventory
            int index = searchInventory(armor, true);
            if (index != -1) {
                int slot = armor.getSlot();
                if (armorSet[slot] != null) {
                    unequipArmor(armor.getSlot());
                }
                armorSet[slot] = armor;
            } else {
                throw new ItemNotFoundException();
            }
        }
    }

    // Unequip armor removes current armor and puts it in the last position in myInventory
    public void unequipArmor(int slot) {
        Armor armor = getEquippedArmor(slot);
        if (armor != null) {
            addItem(armor);
            armorSet[slot] = null;
        }
    }

    public void equipWeapon(Weapon weapon) {
        // Unequips weapon if null
        if (weapon == null) {
            unequipWeapon();
        } else {
            // Searches inventory, only equips if found in myInventory
            int index = searchInventory(weapon, true);
            if (index != -1) {
                if (myWeapon != null) {
                    unequipWeapon();
                }
                myWeapon = weapon;
            } else {
                throw new ItemNotFoundException();
            }
        }
    }

    // Unequip weapon removes current weapon and puts it in the last position in myInventory
    public void unequipWeapon() {
        if (myWeapon != null) {
            addItem(myWeapon);
            myWeapon = null;
        }
    }

    public void optimizeInventory(double maximumWeight) {
        double currentWeight = getTotalWeight();

        if (maximumWeight < 0) {
            throw new IllegalArgumentException();
        } else if (myInventory.size() == 0 || currentWeight == maximumWeight) {
            return;
        } else if (totalEquippedWeight() >= maximumWeight) {
            // Set maximumWeight to zero to drop everything except Double.NaN, weightless items
            maximumWeight = 0;
        }

        // Sorts inventory since not using iterator
        // Iterator only designed to go front to back, need to go back to front
        //  in order to remove starting with lowest value to weight ratio
        sortInventory();
        droppedItems.clear(); // Clears dropped items in case list isn't cleared already
        int idx = myInventory.size() - 1;
        while (idx >= 0) {
            Item item = myInventory.get(idx);
            // Weightless items are not dropped
            if (("" + item.getValueWeightRatio()).equals("NaN")) {
                idx--;
            } else {
                currentWeight -= item.getWeight();
                droppedItems.add(item);
                myInventory.remove(idx);
                if (currentWeight > maximumWeight) {
                    idx--;
                } else {
                    idx = -1;
                }
            }
        }
    }

    public void optimizeEquipment() {
        if (myInventory.size() == 0) // Already as optimized as possible
            return;
        // Armor Slots 0-5, then position 6 is weapon index, stores indices for best equipment;
        int[] bestEquipList = {-1, -1, -1, -1, -1, -1, -1};
        int index = -1;
        Iterator<Item> iterator = inventory();
        while (iterator.hasNext()) {
            Item currentItem = iterator.next();
            index++;
            if (currentItem instanceof Weapon) {
                Weapon currentWeapon = (Weapon) currentItem;
                if (myWeapon == null) {
                    myWeapon = currentWeapon;
                    iterator.remove();
                    index--; // since otherwise indices get thrown off
                } else if (currentWeapon.getDamage() > myWeapon.getDamage()) {
                    bestEquipList[6] = index;
                }
            } else if (currentItem instanceof Armor) {
                Armor currentArmor = (Armor) currentItem;
                int slot = currentArmor.getSlot();
                Armor equippedArmor = getEquippedArmor(slot);
                if (equippedArmor == null) {
                    armorSet[slot] = currentArmor;
                    iterator.remove();
                    index--; // since otherwise indices get thrown off
                } else if (currentArmor.getRating() > equippedArmor.getRating()) {
                    bestEquipList[slot] = index;
                }
            }
        }
        for (int i = 0; i < bestEquipList.length; i++) {
            if (bestEquipList[i] != -1) {
                if (i != 6) {
                    unequipArmor(i);
                    armorSet[i] = (Armor) myInventory.get(bestEquipList[i]);
                } else {
                    unequipWeapon();
                    myWeapon = (Weapon) myInventory.get(bestEquipList[i]);
                }
                myInventory.remove(bestEquipList[i]);

            }
        }
    }

    public static class ItemComparator implements Comparator<Item> {
        public int compare(Item itemOne, Item itemTwo) {
            if (("" + itemOne.getValueWeightRatio()).equals("NaN"))
                return -1;
            if (("" + itemTwo.getValueWeightRatio()).equals("NaN"))
                return 1;
            return (int)(itemOne.getValueWeightRatio() - itemTwo.getValueWeightRatio());
        }
    }
}
