/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package testmethods;

/**
 *
 * @author rjr
 */
public class TestMethods {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        MyMethods test1 = new MyMethods();
        int val = test1.total();
        
        System.out.println("Result " + val);
    }
    
}
