/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package testingstuffch6.pkg8;

/**
 *
 * @author rjr
 */
public class TestingStuffCh68 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        int begw = 0;
        int end = 5;
        
        System.out.println("While loop: ");
        while (begw < end) {
            
            System.out.println("Beginning is " + begw + " in the while");
            begw++;
        }
        
        int begdw = 0;
        System.out.println("Do/While loop: ");
        
        do {
            
            System.out.println("Beginning is " + begdw + " in the do/while");
            begdw++;
        } while (begdw < end);
        
        
        for (int f = 0; f < end; f++) {
            
            System.out.println("F is " + f + " in the for");
        }
        
        String text = "A";
        String grade = "B";
        
        if (text.equals(grade)) {
            
            System.out.println("You got an A!");
        } else if (grade.equals("B")) {
            
            System.out.println("You got a B!");
        } else {
            
            System.out.println("No grades given here!");
        }
        
        
        
        switch (grade) {
        
            case "A":
                System.out.println("That's an A");
                break;
            case "B":
                System.out.println("That's a B");
                break;
            default:
                System.out.println("C or lower");
                
        
        }
        
        int number = 1;
        String animal = "Dog";
        String newAnimal = "Cat";
        
        if (animal.equals(newAnimal)) {
            
            System.out.println(newAnimal.toUpperCase());
            System.out.println(newAnimal.length());
        } else {
            
            System.out.println(animal.toLowerCase());
            System.out.println(animal.length());
        }
        
        String result = (number == 1) ? animal : newAnimal;
        System.out.println(result);
    }
}
    
