/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package concurrentints;
import java.util.*;
/**
 *
 * @author rjr
 */

// Given a set of integers, find the largest number to be made out of them
// ex: 1 2 3 4 would be 4321
public class ConcurrentInts {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        ArrayList list = new ArrayList();
        
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        
        Collections.sort(list);
        Collections.reverse(list);
        
        for (int i = 0; i < list.size(); i++) {
            
            
           System.out.println(list.get(i));
           
        }
    }
    
}
