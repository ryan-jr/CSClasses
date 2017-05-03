/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package assignment1;

/**
 *
 * @author rjr
 */


    
public class Assignment1 {

    /**
     * @param args the command line arguments
     */
    
  
        

    public static void main(String[] args) {
        // TODO code application logic here
        
        Temp test1 = new Temp();
        System.out.println(test1.getValue());
        System.out.println(test1.getScale());
        System.out.println(test1.getTempF());
        
        
        Temp test2 = new Temp();
        test2.setValue(99.1);
        test2.setScale('f');
        
        System.out.println(test2.getValue());
        System.out.println(test2.getScale());
        System.out.println(test2.getTempC());
        System.out.println(test2.getTempF());
        
        System.out.println(test2.comparison(test1, test2));
        
        
    }
    
}
