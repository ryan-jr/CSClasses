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
public class Trex extends Dino{
    
    int arms;
    int claws;
    
    Trex() {
        
        arms = 2;
        claws = 10;
    }
    public void wave() {
        
        System.out.println("Waves at you with tiny arms");
    }
}
