/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package assignment2;

/**
 *
 * @author rjr
 */
public class Apato extends Dino{
    
    private int teeth;
    private int legs;
    
    public void apato() {
        
        this.teeth = 10;
        this.legs = 2;
    }
    
    public void eating() {
        
        System.out.println("MUNCHING ON LEAVES");
    }
}
