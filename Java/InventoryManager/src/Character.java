import java.util.Iterator;

public interface Character
{
    Iterator<Item> inventory();
    void addItem(Item itemTemplate);
    void dropItem(Item item);
    double getTotalWeight();

    Armor getEquippedArmor(int slot);
    int getTotalArmorRating();
    void equipArmor(Armor armor);
    void unequipArmor(int slot);

    Weapon getEquippedWeapon();
    void equipWeapon(Weapon weapon);
    void unequipWeapon();

    void optimizeInventory(double maximumWeight);
    void optimizeEquipment();

    int getAbilityScore(String abilityName);
    void setAbilityScore(String abilityName, int abilityScore);
    int getAbilityModifier(String abilityName);
    boolean checkAbility(String abilityName, int difficulty);

    void addSkill(String skillName, String relatedAbility, int skillRanks);
    int getSkillRanks(String skillName);
    void setSkillRanks(String skillName, int skillRanks);
    String getRelatedAbility(String skillName);
    int getSkillModifier(String skillName);
    boolean checkSkill(String skillName, int difficulty);
}