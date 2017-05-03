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
public class Assignment2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
    
    Apato albert = new Apato();
    Dino don = new Dino();
    Stego sam = new Stego();
        System.out.println(don.getWeight());
    // albert.setWeight(55.2);
    System.out.println(albert.getWeight());
    albert.eating(); 
    albert.sleeping();
    albert.moving();
    
    System.out.println("DON: ");
    don.eating();
    don.sleeping();
    don.moving();
    
        System.out.println("SAM:");
        sam.swing("Sam");
        sam.eating();
        sam.sleeping();
    
    
    }
    
}
