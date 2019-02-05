// Initiates a loop where the user can manage their character
// May also design and implement whatever additional classes and methods needed
// to support this driver so long as you implement every part of the description below

import java.util.Comparator;
import java.util.Scanner;

public class CharacterDriver {
    private CharacterImplementation character = new CharacterImplementation();
    private static final Scanner scan = new Scanner(System.in);


    public static void main(String[] args) {
        CharacterDriver driver = new CharacterDriver();
        System.out.println("=====================================");
        System.out.println("RPG Character Manager!");
        boolean prompt = true;
        while (prompt) {
            driver.printOptions();
            prompt = driver.processOption(driver.getOption());
        }
        System.out.println("This concludes RPG Character Manager.");

    }

    public void printOptions() {
        System.out.println("=====================================");
        System.out.println("Select an option:");
        System.out.println("0: Print character sheet");
        System.out.println("1: Set ability score");
        System.out.println("2: Add skill");
        System.out.println("3: Set skill ranks");
        System.out.println("4: Perform ability check");
        System.out.println("5: Perform skill check");
        System.out.println("6: Quit");
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
                String entry = scan.nextLine();
                option = Integer.parseInt(entry);
                for (int validInt : new int[]{0, 1, 2, 3, 4, 5, 6}) {
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
                printCharacterSheet();
                break;
            case 1:
                setAbilityScore();
                break;
            case 2:
                addSkill();
                break;
            case 3:
                setSkillRanks();
                break;
            case 4:
                performAbilityCheck();
                break;
            case 5:
                performSkillCheck();
                break;
            default:
                return false; // Set prompt to false for "Quit"
        }
        return true; // Set prompt to true for continued management of inventory
    }

    public void printCharacterSheet() {
        Map<String, Integer> abilityToScoreMap = character.getAbilityToScoreMap();
        Map<String, String> skillToAbilityMap = character.getSkillToAbilityMap();
        Map<String, Integer> skillToRankMap = character.getSkillToRankMap();

        ArrayList<String> abilityList = new ArrayList<String>(10);
        ArrayList<String> skillList = new ArrayList<String>(10);

        int i = 0;
        for (ReadonlyMap.Entry<String, Integer> e : abilityToScoreMap.entrySet()) {
            abilityList.add(e.getKey());
        }
        i = 0;
        for (ReadonlyMap.Entry<String, String> e : skillToAbilityMap.entrySet()) {
            skillList.add(e.getKey());
        }
        abilityList.sort(Comparator.naturalOrder());
        skillList.sort(Comparator.naturalOrder());

        System.out.println();
        System.out.println("Ability List: ");
        for (String string : abilityList) {
            System.out.println(string + " score " + abilityToScoreMap.get(string) + " modifier " + character.getAbilityModifier(string));
        }
        System.out.println();
        System.out.println();
        System.out.println("Skill List: ");
        for (String string : skillList) {
            System.out.println(string + " ranks " + skillToRankMap.get(string) + " related ability " + skillToAbilityMap.get(string) + " modifier " + character.getSkillModifier(string));
        }
        System.out.println();
    }

    public void setAbilityScore() {
        boolean scoreSetSuccess = false;
        while (!scoreSetSuccess) {
            int intScore;
            System.out.print("Enter ability score: ");
            String score = scan.nextLine();
            System.out.print("Enter ability name: ");
            String ability = scan.nextLine();
            try {
                intScore = Integer.parseInt(score);
                character.setAbilityScore(ability, intScore);
                scoreSetSuccess = true;
            } catch (Exception e) {
                System.out.println("Invalid entry, try again.");

            }
        }
        System.out.println("Ability Set Successfully.\n");
    }

    public void addSkill() {
        boolean skillSetSuccess = false;
        while (!skillSetSuccess) {
            int intRank;
            System.out.print("Enter skillName: ");
            String skillName = scan.nextLine();
            System.out.print("Enter relatedAbility: ");
            String relatedAbility = scan.nextLine();
            System.out.print("Enter skill Rank: ");
            String skillRanks = scan.nextLine();
            try {
                intRank = Integer.parseInt(skillRanks);
                character.addSkill(skillName, relatedAbility, intRank);
                skillSetSuccess = true;
            } catch (Exception e) {
                System.out.println("Invalid entry, try again.");
            }
        }
        System.out.println("Skill added successfully.\n");
    }

    public void setSkillRanks() {
        int intRank;
        System.out.print("Enter skillName: ");
        String skillName = scan.nextLine();
        System.out.print("Enter skill Rank: ");
        String skillRanks = scan.nextLine();
        try {
            intRank = Integer.parseInt(skillRanks);
            character.setSkillRanks(skillName, intRank);

        } catch (Exception e) {
            System.out.println("Invalid entry, unable to set skill rank, try again.");
            return;
        }
        System.out.println("Skill rank set successfully.\n");
    }

    public void performAbilityCheck() {
        boolean abilityChecked = false;
        while (!abilityChecked) {
            int difficulty;
            System.out.print("Enter ability Name: ");
            String abilityName = scan.nextLine();
            System.out.print("Enter difficulty: ");
            String difficultyString = scan.nextLine();
            try {
                difficulty = Integer.parseInt(difficultyString);
                boolean result = character.checkAbility(abilityName, difficulty);
                System.out.println(abilityName + " " + difficulty + " " + result);
                abilityChecked = true;
            } catch (Exception e) {
                System.out.println("Invalid entry, try again.");
            }
        }
    }

    public void performSkillCheck() {
        boolean skillChecked = false;
        while (!skillChecked) {
            int difficulty;
            System.out.print("Enter skill Name: ");
            String skillName = scan.nextLine();
            System.out.print("Enter difficulty: ");
            String difficultyString = scan.nextLine();
            try {
                difficulty = Integer.parseInt(difficultyString);
                boolean result = character.checkSkill(skillName, difficulty);
                System.out.println(skillName + " " + difficulty + " " + result);
                skillChecked = true;
            } catch (Exception e) {
                System.out.println("Invalid entry, try again.");
            }
        }
    }
}
