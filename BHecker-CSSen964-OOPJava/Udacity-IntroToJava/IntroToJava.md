# Udacity Intro to Java Programming

## Lesson 1 - Introduction

* Compile time errors are syntax errors

* Runtime errors are logic errors

* Algorithims are unambiguous, executable, and terminationg

## Lesson 2 - Objects

```Java

// An example of the Day object and how to add days and get a result


public class Mariner4
{
	public static void main(String[] args)
	{
		Day mariner4 = new Day(1964, 11, 28);
		mariner4.addDays(228); // 1965-07-14
		System.out.println(mariner4.toString());
	}
}

```

* For the above we would look at the Day class.  

* Classes are objects that have the same behavior

* Methods are actions that we can perform on a certain kind of object

* Objects are a thing, methods tell you what that object can do


```

// Program to output # of Sally Ride's days alive

public class DaysAlivePrinter
{
	public static void main(String[] args)
	{
		// Sally Ride was born on May 26 1951
        // Her last day was July 23 2012
        // Use Day objects to calculate and print
        // how many days she lived. 
        // You'll want to use the daysFrom method.
        // Do you expect to get a negative or a positive number of days?
        
        Day birthday = new Day(1951, 05, 26);
        Day lastDay = new Day(2012, 07, 23);
        
        System.out.println(lastDay.daysFrom(birthday));
	}
}

// *** ANOTHER WAY OF WRITING THE ABOVE PROGRAM ***

public class DaysAlivePrinter
{
	public static void main(String[] args)
	{
	    // Hello world
		Day birthday = new Day(1951, 5, 25);
		Day lastDay = new Day(2012, 7 ,23);
		int daysAlive = lastDay.daysFrom(birthday);
		System.out.println(daysAlive);
	}
}

```

A standard method call is done as: OBJECT.METHODNAME(ARG1, ARG2, MOREARGS); // no return value, if there was a return value it would be associated with a variable

* method chaining goes from left to right

```

String hey = "Hello";
hey.toUpperCase(); // HELLO 
hey.toLowerCase(); // hello 
hey.toUpperCase.toLowerCase(); // hello 

// note that hey is still Hello after all of this , because strings are immutable? or pass by ref or pass by value?

```

* Accessors do not change the objects they operate on, e.g. the replace method returns a new string and DOES NOT MODIFY the original string

* Mutators change the methods they operate on

* * Java is pass by ref so:

```

box = new Box
box2 = box;

// Both point to the same object 

Rectangle box = new Rectangle();
Rectangle box2 = box;
box.setColor(Red);
box2.setColor(Blue);

box.fill();
box.draw();

// The above code prints out ONE blue box, because box2 refers to box and the blue setColor command is executed last

```



And

```

String greeting = 
"Hello, World!";
String greeting2 = greeting;
gretting2.toUpperCase();

// The above code proves that toUpperCase will NOT modify strings 
gretting and greeting 2 will BOTH be Hello, World!

```

* IN JAVA INTS/NUMBERS ARE NOT BY REF THEY ARE DIRECT VALUES

```

int num1 = 13;
int num2 = num1; // 13
num2 = 12; // num 2 is now 12

```

* INTS are NOT objects, STRINGS, RECTANGLES, ETC... are objects

* That which is/are objects are passed by ref, primitives are pass by value


```

Lesson 2 Summary
Wow, we learned a whole ton of information in Lesson 2! Let's review what we just learned.

How to construct a new objects that require constructors in one line:

A. For objects that require constructors (e.g. Picture)
Picture rocket = new Picture(“mariner4.jpg”);
Picture: Here we’re telling Java the type of the object we want to construct.
rocket: Here we’re naming the object.
new: Here we’re adding a keyword that tells Java to make a new object.
Picture: Here we’re calling the constructor for the Picture class. What this means is that in the Picture class there is a chunk of code that reads: “public Picture(...) {...}”, and contains information within the brackets about how to actually construct the Picture class from the argument passed in between the parentheses. Don’t worry if this isn’t 100% clear right now; we’ll get plenty of practice with this throughout the rest of the course!
"mariner4.jpg": This is just the necessary argument passed into the Picture constructor.
B. For objects that do NOT require constructors (e.g. String) or non-objects (e.g. int):
int number = 6;
String name = “Dan”;
int/String: The type of the object (or non-object) we’re constructing.
number/name: The name of the object (or non-object)
6/"Dan": The value of the object (or non-object)
What do we mean when we say integers are not “objects”? Read on to find out.

Calling methods on “objects”
For either mutator or accessor methods, use the syntax “.” to call the method named Method on the object named Object.
Now, what do we mean when we say “integers are not objects”? By definition, objects are “things you can call methods on”, and there are no methods you can call on an integer. For example, after writing

int number = 6;
We cannot write things like:

number.multiply(4);
number.add(3);
Instead, we write:

number = number * 4;
number = number + 3;
Variables and references
A common procedure in Java is to construct an object, assign that object “equal to” another object, and then modify the first object. However, if you then change the first object with the mutator object, it changes the second object as well, counterintuitively.

```

```

// Review

* Going over valid variable names in Java

* Going over variable declarations in Java (e.g. double cost = 2.51;, String course = "School";)


* A method that doesn't modify things is an accessor method 

* Method calls are performed left to right 

String state = Mississippi;

state.replace("issipp", "our").length();  // 8 Missouri

* How to construct new objects and NOT assign them to a variable (new Date(2017, 10, 02);)

* System.out.println("45 + 5"); // Outputs 45 + 5, because it's not concatonating things 

```

### Lesson 3 - Classes 


* Accessor methods access information/state 

* Mutator methods update information/state/perform a behavior 

e.g.

```

// Access method call
car1.getGasLevel();

// Mutate method call 
car1.addGas(Double gas)

```

* Instance variables occur in every instance of the class.  

* Things like private String name; are good practice to follow because it encapsulates the variable correctly.

```Java
public class Person {

  private String name;
  private String friends;
  
  public void addFriend(Person friend) {
  
  // Adds friends with space inbetween them using the friend.name method from the friend object.  
  friends = friends + friend.name + " ";
  ```
  
  * instance variable are "long term" and stay with the object as long as it is 'alive'
  
  * Find which use case it is an you then you can narrow it down if you need an instance or a local var 
  
  ```Java
  public class Car {
  
  // Instance Variable 
  private gasInTank;
  
  public void drive(double distance) {
  
  // local var 
  double gasConsumed = distance / milePerGallon;
  
  // updating instance var 
  
  gasInTank -= gasConsumed;
  
  }
  
  }
  ```
  
  
  * With constructors they are the same name as the class, and DO NOT have any return type (not even void), it's just the constructor permission type (publc) followed by the class name and then the parameters, and then the body of the statement 
  
  
  * Look at the following constructors note how you have to create a new object:
  
  ```
  
  public Car(double mpg)
    {
        milesDriven = 0;
        gasInTank = 0;
        milesPerGallon = mpg;
        pic = new Picture("car.jpg");
        pic.draw();
    }

    public Car(double mpg, String pictureFile)
    {
        // TODO: Complete this constructor
        milesPerGallon = mpg;
        pic = new Picture(pictureFile);
        pic.draw();
    }
	
	
	```
	
	* Remember, instance variables store long term/persistent data like the friends you have, if you wanted to print out the friends you had, you would access it through the getFriends method which only returns the instance variable friends. 

* SOME CONFUSING CODE/CONSTRUCTOR

public class Person
{
    private String name;
    private String friends;
    
    // TODO #1: Fill in the rest of the arguments to the Person constructor
    // The Person constructor should take in 3 additional arguments:
    // 1) String pictureName
    // 2) int xCoord
    // 3) int yCoord
    public Person (String aName, String pictureName, int xCoord, int yCoord)
    {
        name = aName;
        friends = "";
        
        // TODO #2: Fill in the rest of this constructor
        //
        // You need to create a local variable called picture and assign to
        // picture the picture that we want to use.
		
		// *** THIS LINE IS CONFUSING ***
		// Create a Picture object named picture and that new Picture Object should pull from a specified paramater that was passed in 
          Picture picture = new Picture(pictureName);
        // You need to move the picture to xCoord and yCoord.
        // You can move the picture object by calling the translate method.
         picture.translate(xCoord, yCoord);
        // The last step is to draw the picture.
        picture.draw();
    }	
	
	```
	
	* That which is being passed into the constructor/which is declared in the constructor is NOT an instance variable 
	
	* For java docs we explain the function in the comments and then for every paramater we @param paramater name, and explain the paramater that is being taken 
	
	* If we use a type in front of a variable name that has the same name as an instance variable, we've now redeclared it as a local variable.  
	
	* We can use this declaration in front of instance variables, because it refers to this instance variable that you want.  
	
	```
	
	public class Person {
	
	private String name;
	
	public Person (String name) {
	
	this.name = name; // assigns the PARAMATER name to the INSTANCE VARIABLE NAME
	}
	
	}
	```
	
	* You can also use this to pass a paramater if you so choose  such as friend.addFriend(this);
	
	* For javadocs we use @param "TEXT" to describe paramaters, and we use @return "TEXT" to describe the return values
	
	* An explicit paramater is the one that's being passed, an implicit paramater is one that's being called on such as this.
	
	* Remember, you can have an instance variable, that is accessed by a constructor and set to a default value. 

***

### Lesson 4 - Fundamental data types 

*  We know int and double, but there are more complex data types

* Int can only hold up to about 2 billion before it wraps around

* Doules can have an issue especially with percision/rounding

* we can make a constant using the word FINAL


* To get input from a user we use Scanner x = new Scanner(System.in);

* We use the methods of the scanner class on the variable such as int age = x.nextInt(); or double weight = x.getDouble();

* To format print things we use printf("%8.2f\n", totalPrice);

* In the above we note that we want the string to be 8 spaces in, with 2 decimal points, that it's a floating point number totalPrice, and that we want a newline after 

* We use %s for strings, and %d for ints with the printf statement 

***

### 5.1 - Decisions

***

### 5.2 - Decisions 2

* When you compare 2 decimal numbers compare wether or not they are close to each other, not wether or not they are exactly the same.  We do this by taking the value of epsilon

* == checks to see if objects are exactly the same/point to the same point in memory 

* When comparing strings use the equals method like so:
firstAndSecond.equals(STRING_BEING_COMPARED_)

* You can set booleans to complicated conditions and return them.  for instance here we have a method that returns a boolean value and takes 2 paramters

```
private Picture pic;
private int width;
private int height;

public boolean isInMiddle(int x, int y) {

boolean xInMiddle = x >= width / 3 && x < width * 2 / 3;

boolean yInMiddle = y >= height / 3 && y < height * 2 / 3;

return xInMiddle && yInMiddle;

}
```

* in.hasNextInt() checks to see if a user puts in an integer, and returns a boolean value.  

***

### 6.1 - Loops

* When you know how many iterations you want use a for loop, if you don't know how many iterations use a while loop

```Java

// String traversal with a vowel counter 

int count = 0;

for (int i = 0; i < word.length(); i++) {

String letter = word.substring(i, i + 1);

if ("aeiouAEIOU".contains(letter)) {

count++;

}
}
```


```Java 

// String traversal, character replacement

public class Twitterizer
{
    /**
     * Shortens and returns long posts by removing vowels
     * @param longPost the post whos vowels need to be removed
     * @return a version of the post without vowels
     */
    public String shorten(String longPost)
    {
        // YOUR CODE HERE
        for (int i = 0; i < longPost.length(); i++) {
            
            String letter = longPost.substring(i, i + 1);
            
            
            if("aeiouAEIOU".contains(letter)) {
                
                longPost = longPost.replace(letter, "");
            }
            
           
        }
         return longPost;
    }
}


```

* To reverse a string without stringbuilder we start at the last letter, add that letter to a string and do so repeatedly with a loop

* To add a specific character to a string we use a construct like: 

```

message = message + stringWereReadingFrom.substring(i, i + 1);

```

* When counting if a form loop if i = x and i <= y.  Then there are y - x + 1 values that will be printed.  if you only wnated to print out a set number of values

```
// Looping through and counting constants 

int result = 0;
for (int i = 0; i < word.length(); i++) {

String letter = word.substring(i, i + 1);

if (! "aeiou.contains(letter.toLowerCase())) {

result++;

}
}

```

***

### 6.2 - Loops 

```
do {
// code 

} while (condition);
```

* Do loops enter the loop at least once, whereas a while loop might not. 

* Sentinal values are values that are guaranteed to end a loop 

* To read from a file we use the scanner class  like so:

```

File inputFile = new File("input.txt");
Scanner in = new Scanner(inputFile);
```

* We need to deal with the possibility in the above code that there is no file named input.txt, and to do that we would add throws FileNotFoundException underneat public static void main(String[] args)

* For the file itself we would read it using while(in.hasNextDouble()) // Example could also be string, ints etc...
{
double val = in.nextDouble();


```

// Reading input from a file and finding the largest value 

File inputFile = new File("input.txt");
Scanner in
 
 
 Scanner in = new Scanner(inputFile);
 
 double larges = in.nextDouble();
 
while (in.hasNextDouble()) {

double input = int.nextDouble();
if (input > largest) {

largest = input;
}
}
System.out.println("Largest value is: " + largest);
}
```

```
// File to read country populations AND country name 

String country = in.next();
double population = in.nextDouble();
double largest = population;
String largestCountryName = country;

while (in.hasNext()) {

country = in.next();
population = in.nextDouble();
if population > largest) {
largest = population;
largestCountryName = country;
}
}
System.out.println("Largest Country: " + country;
System.out.println("The population size is: " + population);

```

* Common algos include average, finding the largest element, counting matches, finding the first match, position of the first match, finding all matches, etc

```

// Getting the number of digits in a string 

int count = 0;
number = 269;
temp = number;

while (number > 0) {

int digit = temp % 10 // gets the last digit 
temp = temp / 10;

count++;
}
```

```Java 

public class FirstMatch
{
    public static void main(String[] args) throws java.io.FileNotFoundException
    {
        Scanner in = new Scanner(new FileReader("aliceInWonderland.txt"));
        String longWord = "";
        boolean found = false;
        final int THRESHOLD = 9;
        // TODO: Write a loop that searches for long words
        // (more than THRESHOLD letters)
        // The loop should stop if you find one or if you run out of words
        
        while (in.hasNext() && !found) {
            
            // We can't just use in.next.length() in the if condtion because if we use 
            // in.next() and attempt to assign it to longword, it will get the word AFTER
            // the word that met the threshold
            String word = in.next();
            if (word.length() > THRESHOLD) {
                
                longWord = word;
                found = true;
            }
        }
        System.out.println("The first long word is: " + longWord);
    }
}

```

* For printing a pyramid row we need to first do a for loop set to the number of rows we want and then another for loop for the column.  It's the outer for loop condition that changes/updates in order to accomidate what's being printed

 * We can use random generators through using 
 
```
 Random generator = new Random();
 
 int randomInt = generator.nextInt(n)

```
 
* A die generator would look like: 

```

sides = s;
final int SEED = 42;
generator = new Random(SEED);

System.out.println(1 + gnerator.nextInt(sides);
```

* For debuggers the key concepts we need are breakponts, single steps, and inspect variables 