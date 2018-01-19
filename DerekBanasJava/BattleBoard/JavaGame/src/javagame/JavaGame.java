/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javagame;

/**
 *
 * @author rjr
 */
public class JavaGame {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        MonsterTwo.buildBattleBoard();
        
        char[][] tempBattleBoard = new char[10][0];
        
        MonsterTwo[] Monsters = new MonsterTwo[4];
        
        Monsters[0] = new MonsterTwo(1000, 20, 1, "Frank");
        Monsters[1] = new MonsterTwo(500, 40, 2, "Drac");
        Monsters[2] = new MonsterTwo(1000, 20, 1, "Paul");
        Monsters[3] = new MonsterTwo(1000, 20, 1, "George");
        
        MonsterTwo.redrawBoard();
    }
    
}
