/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dog;

/**
 *
 * @author rjr
 */
public class Dog {

    /**
     * @param args the command line arguments
     */
    
    public static int legs = 4;
    boolean bark = true;
    static int dogCount = 0;
    
    public Dog() {
        
        dogCount++;
    }
    
    public static void barking(boolean status) {
    
        if (status == true) {
            
            System.out.println("Bark Bark");
        } else {
            
            System.out.println("...");
        }
}
    
    public static void main(String[] args) {

       Dog fido = new Dog();
       fido.bark = false;
       
        System.out.println(fido);
        fido.barking(fido.bark);
        System.out.println(fido.legs);
        
        Dog spot = new Dog();
        
        spot.barking(spot.bark);
        spot.legs = 3;
        System.out.println(spot.legs);
        System.out.println(fido.legs);
        
        System.out.println("There are " + dogCount + "dog(s)");
       
    }
    
}
