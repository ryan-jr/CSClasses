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
public class Dino {
    
    private double height;
    private double weight;
    private double speed;
    private String diet;
    
    
     Dino() {
        
        
        height = 22;
        weight = 10;
        speed = 30;
        diet = "FOOD!";
        
    }
    public void eating() {
        
        System.out.println("This dino is eating");
    }
    
    
    public void moving () {
        
        System.out.println("This dino is moving at " + this.speed + " kph");
    }
    
    public void sleeping() {
        
        System.out.println("ZZZ...");
    }
    
    // Accessor methods (setters)
    
    public void setHeight(double hgt) {
        
        this.height = hgt;
    }
    
    public void setWeight(double wgt) {
        
        this.weight = wgt;
    }
    
    public void setSpeed(double spd) {
        
        this.speed = spd;
    }
    
    public void setDiet(String dt) {
        
        this.diet = dt;
    }
    
    // Accessor methods (getters)
    
    public double getHeight(){
        
        return this.height;
    }
    
    public double getWeight() {
        
        return this.weight;
    }
    
    public double getSpeed() {
        
        return this.speed;
    }
    
    public String getDiet() {
        
        return this.diet;
    }
    
}
