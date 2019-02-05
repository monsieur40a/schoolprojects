// fort0142

public class Main {
    public static void main(String[] args) {
        BattleBoats battleBoatsGame = new BattleBoats();
        BattleBoatsBoard gameBoard = battleBoatsGame.initializeBoard();
        battleBoatsGame.startGamePlay(gameBoard);
    }
}
