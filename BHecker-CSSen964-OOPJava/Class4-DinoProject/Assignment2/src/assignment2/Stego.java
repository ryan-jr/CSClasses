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
public class Stego extends Dino{
    
    int spikes;
    boolean scales;
    
    Stego() {
        
        spikes = 22;
        scales = true;
    }
    
    public void swing(String stegoName) {
        
        System.out.println(stegoName + "swings their tail in your direction!");
    }
}
