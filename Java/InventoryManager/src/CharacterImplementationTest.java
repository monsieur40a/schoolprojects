import org.junit.Test;

import java.util.Iterator;
import java.util.NoSuchElementException;

import static org.junit.Assert.*;
import static org.junit.Assert.assertTrue;

public class CharacterImplementationTest {

    //Tests whether duplicate item references trigger ItemNotFound after its been removed
    @Test(expected = ItemNotFoundException.class)
    public void dropItemTestOne() {
        CharacterImplementation c = new CharacterImplementation();
        Item item = new ItemImplementation();
        ((ItemImplementation) item).setName("");
        ((ItemImplementation) item).setGoldValue(200);
        ((ItemImplementation) item).setWeight(3);
        c.addItem(item);
        Iterator<Item> iterator = c.inventory();
        Item item2 = iterator.next();
        c.dropItem(item2);
        c.dropItem(item2);
    }

    // Tests if item is actually removed from Inventory
    @Test(expected = NoSuchElementException.class)
    public void dropItemTestTwo() {
        CharacterImplementation c = new CharacterImplementation();
        Item item = new ItemImplementation();
        ((ItemImplementation) item).setName("");
        ((ItemImplementation) item).setGoldValue(200);
        ((ItemImplementation) item).setWeight(3);
        c.addItem(item);
        Iterator<Item> iterator = c.inventory();
        Item item2 = iterator.next();
        c.dropItem(item2);
        Iterator<Item> iterator2 = c.inventory();
        Item item3 = iterator2.next();
    }

    @Test(expected = NullPointerException.class)
    public void dropItemTestThree() {
        CharacterImplementation c = new CharacterImplementation();
        c.dropItem(null);
    }

    // Tests ItemNotFoundException, with armor not yet added to inventory
    @Test(expected = ItemNotFoundException.class)
    public void equipArmorTestOne() {
        CharacterImplementation c = new CharacterImplementation();
        Armor armor = new ArmorImplementation();
        ((ArmorImplementation) armor).setSlot(0);
        ((ArmorImplementation) armor).setRating(10);
        ((ArmorImplementation) armor).setName("hello");
        ((ArmorImplementation) armor).setGoldValue(900);
        ((ArmorImplementation) armor).setWeight(5);
        c.equipArmor(armor);
    }

    // Tests whether null unequips armor
    @Test
    public void equipArmorTestTwo() {
        CharacterImplementation c = new CharacterImplementation();
        Armor armor = new ArmorImplementation();
        ((ArmorImplementation) armor).setSlot(0);
        ((ArmorImplementation) armor).setRating(10);
        ((ArmorImplementation) armor).setName("hello");
        ((ArmorImplementation) armor).setGoldValue(900);
        ((ArmorImplementation) armor).setWeight(5);
        c.addItem(armor);
        Iterator<Item> iterator = c.inventory();
        Armor armor2 = (Armor)iterator.next();
        c.equipArmor(armor2);
        Armor armor3 = c.getEquippedArmor(0);
        assertTrue(armor3 != null);
        c.equipArmor(null);
        assertTrue(c.getEquippedArmor(0) == null);
    }

    // Tests whether equipArmor equips Armor
    @Test
    public void equipArmorTestThree() {
        CharacterImplementation c = new CharacterImplementation();
        Armor armor = new ArmorImplementation();
        ((ArmorImplementation) armor).setSlot(0);
        ((ArmorImplementation) armor).setRating(10);
        ((ArmorImplementation) armor).setName("hello");
        ((ArmorImplementation) armor).setGoldValue(900);
        ((ArmorImplementation) armor).setWeight(5);
        c.addItem(armor);
        Iterator<Item> iterator = c.inventory();
        Armor armor2 = (Armor)iterator.next();
        c.equipArmor(armor2);
        Armor armor3 = c.getEquippedArmor(0);
        assertTrue(armor2 == armor3 && armor3 != null);
    }

    // Tests ItemNotFoundException, with weapon not yet added to inventory
    @Test(expected = ItemNotFoundException.class)
    public void equipWeaponTestOne() {
        CharacterImplementation c = new CharacterImplementation();
        Weapon weapon = new WeaponImplementation();
        ((WeaponImplementation) weapon).setDamage(0);
        ((WeaponImplementation) weapon).setName("hello");
        ((WeaponImplementation) weapon).setGoldValue(900);
        ((WeaponImplementation) weapon).setWeight(5);
        c.equipWeapon(weapon);
    }

    // Tests whether null unequips weapon
    @Test
    public void equipWeaponTestTwo() {
        CharacterImplementation c = new CharacterImplementation();
        Weapon weapon = new WeaponImplementation();
        ((WeaponImplementation) weapon).setDamage(0);
        ((WeaponImplementation) weapon).setName("hello");
        ((WeaponImplementation) weapon).setGoldValue(900);
        ((WeaponImplementation) weapon).setWeight(5);
        c.addItem(weapon);
        Iterator<Item> iterator = c.inventory();
        Weapon weapon2 = (Weapon)iterator.next();
        c.equipWeapon(weapon2);
        Weapon weapon3 = c.getEquippedWeapon();
        assertTrue(weapon3 != null);
        c.equipWeapon(null);
        assertTrue(c.getEquippedWeapon() == null);
    }

    // Tests whether equipWeapon equips Weapon
    @Test
    public void equipWeaponTestThree() {
        CharacterImplementation c = new CharacterImplementation();
        Weapon weapon = new WeaponImplementation();
        ((WeaponImplementation) weapon).setDamage(0);
        ((WeaponImplementation) weapon).setName("hello");
        ((WeaponImplementation) weapon).setGoldValue(900);
        ((WeaponImplementation) weapon).setWeight(5);
        c.addItem(weapon);
        Iterator<Item> iterator = c.inventory();
        Weapon weapon2 = (Weapon)iterator.next();
        c.equipWeapon(weapon2);
        Weapon weapon3 = c.getEquippedWeapon();
        assertTrue(weapon2 == weapon3 && weapon3 != null);
    }

    //Tests whether addItem with null argument throws exception
    @Test(expected = NullPointerException.class)
    public void addItemTest() {
        CharacterImplementation c = new CharacterImplementation();
        c.addItem(null);
    }

    @Test(expected = IllegalArgumentException.class)
    public void getEquippedArmor() {
        CharacterImplementation c = new CharacterImplementation();
        c.getEquippedArmor(9);
    }



}