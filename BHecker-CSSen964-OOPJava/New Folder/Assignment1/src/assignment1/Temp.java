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
public class Temp {
    
    private double temp;
    private char scale;
    
    
    
    public static int compare(Temp A, Temp B) {
        
        return 1;
    }
    
    // CONSTRUCTOR METHODS
    Temp() {
        
        temp = 0;
        scale = 'c';
    }
    
    Temp(double value) {
        
        this();
        temp = value;
    }
    
    Temp(char x) {
        
        this();
        scale = x;
    }
    
    Temp(double value, char x) {
        
        this.temp = value;
        this.scale = x;
    }
    
    // ACCESSOR METHODS SETTERS/GETTERS
    public void setValue(double value) {
        
        this.temp = value;
    }
   
    public void setScale(char x) {
    
       this.scale = x; 
    }
    
    public void setValueAndScale(double value, char x) {
        
        this.scale = x;
        this.temp = value;
    }
    
    
    public double getValue() {
        
        return temp;
    }
        
    public char getScale() {
        
        return scale;
    }
    
    
    public double getTempF() {
        
        if (scale == 'f') {
            
            return temp;
        } else {
            
            return (9 * (temp / 5) + 32);
        }
        
    }
    
    public double getTempC() {
        
        if (scale == 'c') {
            
            return temp;
        } else
            
            return (5 * (temp - 32) / 9);
        }
    
    public int comparison(Temp a, Temp b) {
        
        // checks scale, now need to check temp value
        
        if (a.getScale() == b.getScale()) {
            
            if (a.getValue() > b.getValue()) {
                
                return 1;
            } else if (a.getValue() == b.getValue()) {
                
                return 2;
            } else {
                
                return 3;
            }
            
            
        } else
            
            if (a.getTempC() > b.getTempC()) {
                
                return 4;
            } else if (a.getTempC() == b.getTempC()) {
                
                return 5;
            } else {
                
                return 6;
            }
        
            
    }

}
