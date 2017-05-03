/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication18;

/**
 *
 * @author rjr
 */

class Animal {
    
    String name;
    String type;
    
    public void speak(){
    
        System.out.println(name + " the " + type + " says wheeee!");
    }
    
}
public class JavaApplication18 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Animal a1 = new Animal();
        Animal a2 = new Animal();
        
        a1.name = "Wally";
        a1.type = "Wallabee";
        a2.name = "Kat";
        a2.type = "Kangaroo";
        
        
        
        a1.speak();
        a2.speak();
    }
    
}
