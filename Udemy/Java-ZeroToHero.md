# Udemy Java Zero to Hero


### Section 5 Lesson 31

* Method overloading is naming the method the same (such as calculateTemp) but passing that method a different number of args/paramters.  

* Changing the return type of an overloaded method does NOT change the signature



```Java

// Section 5 Lesson 31 Challenge

import java.util.*;

class Main {
  
  public static double convertImperialToMetric(double feet, double inches) {
    
    if (feet >= 0 && inches >= 0 && inches <= 12) {
      
      double convertedValue = (inches * 2.54) + (feet * 12 * 2.54);
      return convertedValue;
    } else {
      
      return -1;
    }
  }
  
  public static double convertImperialToMetric(double inches) {
    
    if (inches >=0) {
      
    double feet = (int) inches / 12;
    double convertedInches = (int) inches % 12;
    return convertImperialToMetric(feet, 0);
    } else {
      
      return -1;
    }

    
  }
  
  public static void main(String[] args) {
    System.out.print(convertImperialToMetric(1, 10));
    System.out.print("cm");
    System.out.println();
    System.out.println(convertImperialToMetric(99));
    
    for (int i = 0; i < 100; i++) {
      
      double rand = (double)(Math.random() * 100);
      System.out.println("Random Number: " + rand);
      System.out.println(convertImperialToMetric(rand));
    }
    
  }
  
  
}

```

## Section 6 Lesson 1

* If/else statements and switch statements are for control flow/branching, but if there are a lot of branches to go through, usually case statements are preferable.  

* Switch statements in Java 8 allow for string statments to be tested.  To accurately test them it is best to use .toLowerCase() or .toUpperCase() in the switch to ensure compatability.  


## Section 6 Lecture 36

```

// Even testing example code

class Main {
  
  
  public static void main(String[] args) {
    
    int count = 0;
    
    for (int i = 0; i < 100; i++) {
      
      if (i % 2 == 0 && count <= 5) {
        
        System.out.println("Even #: " + i);
        count++;
        System.out.println("Number of even #'s: " + count);
        
        
      } else if (i % 2 != 0 && count >= 5){
        
        break;
      } else {
        
        continue;
      }
      
    }
  }
}

```

### Section 7 Lesson 37

* State is a property, behavior is an action

* Software objects have state (fields) and behavior (methods)

* Classes often have class/memember variables AKA: fields

* Encapsulation hides away the internal workings of a field/part of a class, in order to do this with class variables we set them to private


### Section 7 Lesson 38

* The this keyword specifies member variables/fields from paramaters, for instance:

```Java

public class Car {
	
	private String model;

	// Setter
	public void setModel(String model) {

	// We tell the difference between the field model and the paramater model by letting the method know that we set the field model by using the this keyword in front of it.  

	this.model = model;
	}

	// Getter
	public void getModel() {

	return this.model;
	}
}



```

* A class is a blueprint for objects

### Section 7 Lesson 39

* You can call a constructor within a constructor

* Constructors HAVE TO HAVE THE SAME NAME AS THE CLASS, they can also be overloaded, and have different paramaters.  

* With constructors we set the fields/member variables that we want given a set of paramaters.  

* To call a constructor within a constructor we would do:

```
this(1, "ABC", 123);

// If we call a constructor within a constructor it must be the first line of the constructor.  

```

* It is considered best practice to call the constructor directly on the field as opposed to calling the setter.  


```Java

// Inside a constructor for a bank Account:

// Right
this.acctNumber = number;

// Wrong
// While this is possible within the constructor, it is bad form
setNumber(number);

```

* The general rule of thumb is you only call a constructor within a constructor, not a getter/setter


