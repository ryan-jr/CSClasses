# Barbara Hecker

## Sen 894 Object Oriented Java Programming Summer 2012

### http://web.archive.org/web/20121124115311/http://www.bhecker.com:80/itu/viewforum.php?f=2

### https://www.youtube.com/watch?v=HMUkS0sJr70&list=PL07BAEC9E3E9E49F3


#### Lecture 1: General Class overview (nothing you need)

#### Lecture 2: Overview of Java (Behind by 1 because This is the first lecture/powerpoint)

* Java

* Developed by Sun(James Gosling)

* Gneral purpose OO language based on C/C++

* Designed for easy Web/Internet apps

* Wide acceptance

* Java Features

* Simple, and fixes some clumsy features of C++, no pointers, automatic garbage collection, and a large class library

* OO, with a focus on data/objects and methods manipulating the data, all functions are associated w/ objects, w/ almost all data types are objects(files, strings, etc...), has potentially better code org/reuse

* Interprted, Java generates byte code NOT native machine code, the compiled byte code is platform independent and translated on the fly to machine readable instructions by the JVM

* Portable, The same apps run on all platforms with the size of primitive data types are always the same with the libraries defining portabile interfaces

* Reliable, extensive compile-tiem and runtime error checking, no pointers, but real arrays, Memory corruptions are unauthorized memory access are impossible with automatic garabe collection which tracks object usage over time

* Secure, usage in networked enviros requires more security and the memory allocation model is a major defense, and access restrictions are forced(private, public, etc..)

* Multithreaded, multiple concurrent threads can run simeultaneously and utilizes a sophisticated set of synchronization primitives

* Dynamic, Java is designed to adapt to evoloving enviro, libraries can freely add new methods/instance variables wo/o any effect on their clients, interfaces promote flexibility/reusability in code by specifying a set of methods an object can perform, but leaves open how these methods should be implemented and can check the class type in runtime

* Java Disads

* Slower than a compiled langauge such as C (up to 3 to 4x slower)

* Language basics

* Data types (8 primitives: boolean, byte, short, int, long, float, double, char)

* Class types (Either provided by Java, or made by programmers: String, Integer, Array, Frame, Object, Person, Animal)

* Flow control (if, if-else, if-else if, switch, for, while, do-while, break, continue)

```Java

int x;
boolean b = true;
Frame win = new Frame();
String x = "How are you?";
int[] intArray;
intArray = new int[2];
intArray[0] = 12;
intArray[1] = 6;
Person pArray = new Person[10];

```

* A class is a template for an object and instatiates it


#### Lecture 2: OOP

* Procedural vs OOP

* The unity of procedural programming is the function, a unit in OOP is the class

* Procedural programming concentrates on creating functions, while OOP starts from isolatin gthe classes and then looks for the methods inside the classes

* Procedural programming separtes data of the program from the ops t
* A class can have 3 kinds of members, fields(variables, member data): data variables which deterhat maniuplate the data, while OOP focuses on both data and ops

* Concept of Class and Object

* Class refers to a blueprint, it defines the vars and methods the objects support, Object is an instance of a class, each object has a class which defines its data and behavior

* Class members
mine the status of the class or an object, methods(member functions): executable code of the class built from statements.  It allows us to manipulate/change the status of an object or access the avlaue of the data member, or nested classes/interfacesfunctionality

* identity determines what the object is supposed to be/do, fields determine state, methods determine behavior/

* Fields: Declaration

* Field declaration has a type name followed by the field name and potentially an initialization clause

* Primitive data type(boolean, char, byte, short, int, long, float, double) vs. Obj refs

* Field delcarations can be preceded by different modifiers including access control, static, final, etc...

* Access control modifiers: private: private members are acessible only in the class itself, package: package members are acessible in classes in the same package and the class itself, protected: proteced members are accessible in classes in the same package subclasses of the class and the class itself

```Java

// Sample class

class Penicl {
	
	// Instance variables
	public class String  ****color = "red";
	public int length;
	public float diameter;


	// Class variable (all instances share this variable)
	// Static basically controls all instances of a class(god mode/controls all pencils/members of a class in some way)
	public static long nextID = 0;


	public void setColor(String newColor) {

		// setter/accessor
		****color = newColor;	// Note that color is the same one above, and color is essentailly a 'global' variable in this case (although the idea of global/local vars could get us into trouble if we think about it too much)
	}

	public string getColor() {

		// getter/accessor
		return color;
	}
}

```

* Field modifiers

* Static, only one copy of static exists which is shared by all objects of the class, and can be accessed directly in the class itself, access from outside of the class must be preceeded by the class name (Pencil.nextID);, or it can be accessed by an object belonging to the class (from outside the class non-static fields must be accessed through an object ref).

* Final once intialized means that the value cannot be cahnged and is often used to define constants, static final fields must be initialized when the class is initialized, non-static final fields must be initilized when an object of the class is constructed

* Field intialization

* Field initialization is not neccessary to be constants, as long as it has the right type, if there is no initalization then there will be a default value assigned (boolean:false, char:'\u0000', byte/short/int/long:0, float: +0.0f, double: +0.0, object ref: null)

* Method declaration

* Comes in 2 parts: Header: Consists of modifiers(optional), return type, method name, paramater list and a potential throws clause(optional), there are also types modifiers (access control, abstract , static, final), Method body: Method body


* Method Invocation

* Method invocations are invoked as ops on the objects/classes using the dot(.) operator(refrence.method(args), static methods are outsided of the class ref and can either be the class name or an objcet ref belonging to the class, insied the class ref can be omitted,  in non-static method: ref must be an obj ref

* Method Overloading

* A class can have more than one method with the same name as long as they have a different paramater list

* Methods(Paramater values)

* Paramaters are always passed by value 

*  Main method(Concept)

* Main method is one in shich the system locates/runs the main method for a class when you run a program, other methods get execution when called by the main method explicitly/implicitly

* Main can get input from the command line via args

* Class modifiers

* A class also has modifiers: Publc: publically accessible, w/o this modifier a class is only accessible w/in its own package.  Abstract: no objects of abstract classes can be crated, all of its abstract methods must be implemented by its subclasses otherwise that subclass must be declared abstract also.  Final: Cannot be subclassed.  

* Normally a file can contain multipel classes, but only one public one.  The file name and the public class name should be the same.  



```

OOP is PIE

P: Polymorphism (System.out.println is an example of poly b/c it can take diff paramaters and print them out just fine (int, float, double, string, char, etc...))
I: Inheritance
E: Encapsulation(Information hiding, simplifying the details(engine))

* Main should usually be short (half a dozen lines or so), this is because Main is the manager, the classes are the ones who do the work
```

***

#### Lecture 3: OOP

* Object creation


```Java

Body sun = new Body();

```

* An object is created with the new method in which the JVM/runtime will allocate enough memory to store the new object, and if there is not enough space the JVM will try to reclaim space from no longer used objects, if there is still not enough memory then it will throw an OutOfMemoryError

* Constructor

* These are ways to initilize an object before the ref to the object is returned by new and has the same name of the class and can have any of the same access modifiers as class members.  

* Constructors are similar to methods, a class can have multiple constructors as long as they have diff paramaters, but have NO return type.  

* There are no arg constructors, but if no constructor is provided explicitly by the programmer than the language provides a default no arg consructor


```Java

// Constructor example

class Body {
	
	private long idNum;
	private String name = "empty";
	private Body orbits;
	priave static long nextID = 0;

	Body() {

		idNum = nextID++;
	}

	Body(String bodyName, Body orbitsAround) {

		this();				// Declaring this in such a way automatically means that all of the variable names have this. in front of them
		name = bodyName;	// Without this() we could do this.name;
		orbits = orbitsAround;	// Without this() we could do this.orbits;
	}
}

Body sun = new Body();	// Assume no body object is constructed before	(idNum is 0, name is empty, orbits is null) (calls first constructor)



// NOTE: THE DEFAULT/NO ARG CONSTRUCTOR WILL ALWAYS/AUTOMATICALLY TRIGGER! THIS IS WHY WE DO NOT NEED idNum = nextID++; IN THE SECOND STATMENT!!!
// THIS MEANS YOU SHOULD SET THE DEFAULT CONSTRUCTOR TO HANDLE THINGS THAT WILL ALWAYS HAPPEN/BE DONE FOR EVERY INSTANCE OF THE CLASS!!!

Body sun = new Body("Sol", null);	// Assume no Body object is constructed before (These next two are separate from the above example) (idNum is 0, name is Sol, orbits null) (calls second constructor)
Body earth = new Body("Earth", sun);	(idNum is 1, name is Earth, orbits sun) (calls second constructor)

```

* Using this

* Inside a constructor you can use this to invoke another constructor in the same class which is known as explicit constructor invocation.  It must be the first statement in the constroctor body if it exists.  This can also be used as a ref of the current object, it CANNOT be used in a static method.  

* this is much like super (and goes up to the hierarchy), super goes up the hierarchy above it, this refers to the class itself and what specifically is being constructed etc...


```


// NOTE: THE DEFAULT/NO ARG CONSTRUCTOR WILL ALWAYS/AUTOMATICALLY TRIGGER! (AND ALSO WHEN USING THIS) THIS IS WHY WE DO NOT NEED idNum = nextID++; IN THE SECOND STATMENT!!!
// THIS MEANS YOU SHOULD SET THE DEFAULT CONSTRUCTOR TO HANDLE THINGS THAT WILL ALWAYS HAPPEN, THIS IS GOOD FOR CONSISTENCY
// THIS IS NORMALLY USED TO REF/TRIGGER THE DEFAULT CONSTRUCTOR


```

* Other intilization methods

* Intiilization block (a block of statmetns to initalize fields of the object), outside any member or constructor declaraions are exectued before the body of the constructors

* Static iniliazation block resemble a non-static inlitlization block execpt that it is declare static, can only ref to static members and cannoth throw checked exceptions and gets executed when the class fs first loaded.  

* Packages

* Classes can be groupd in a collection called a package, Java's standard library consists of hierarchal packages, such as java.lang and java.util

* THe main reason to use packages is to guarantee uniqueness of class names, classes with same names can be encapsulated in different packages.  The tradition of package name is to reverse of the company's internet name

* Class importation

* THere are two ways of accessing ublic classes of another package 

* 1: Explicitly give the full package name before the class name

```Java

java.util.Date today = new java.util.date();

```

* 2: Import the package via import (below the package statement)

```Java

// Single class import
import java.util.Date();

Date today = new Date();

// Everything from the class import

import java.util.*
Date today = new Date();

```

* If there is a naming conflict (say between java.util.* and java.sql.*)

```Java

Date today = new Date(); // ERROR: java.util.Date or java.sql.Date?

```

* In the above example if you only need one of them, import that class explicitly

* If you need both of them you have to use the full package name before the class ane

```

import java.sql.*;
import java.util.*;

java.sql.Date today = new java.sql.Date();
java.util.Date nextDay = new java.util.Date();

```

* Encapsulation of classes into a package

* 2 steps: 1.  Put the name of the package at the top of the source file.  2.  put the files in a package into a subdir which mathces the full package name

* Usually the above is done automatically


* Improving data encapsulation

* We can improve on data encapsulation in the Body program in a a couple/few ways: 1.  Setting the fields/instance and class variable(s) to private, and 2.  by creating accessor methods (getters/setters)

```Java

class Body {
	
	private long idNum;
	private String name = "<unnamed>";
	private Body orbits = null;
	private static long nextId = 0;

	Body() {

		idNum = nextId++;
	}

	Body(String bodyName, Body orbitsAround) // This is why Body earth = new Body("earth", sun); is a thing b/c the 2nd arg may/may not be of the Body class
}


```Java

// Project1

```

* Sets are normally void, gets return values

***

Lecture 4: 

* Note how in the constructor methods that only are getting passed 1 paramater that we still have to use this(); at the top, this is because the other value still has to be set.  E.g. if we are only passed the temp, we still have to set the scale from the default constructor.  

* STARTING ON PPT 4: Inheritance

* Concept

* Inheritance means you can create new classes that are built on exsiting classes and can reuse the xisting class's methods/fields and add new methods/fields to adapt new classes to new situations using superclasses and subclasses

* Subclass B IS-A subclass of Superclass A

```

public class Person {
	
	// Code for person class here
}

public class Student extends Person {
	
	// More stuff here

	// Default constructor
	public Student() {

		super();	// Calls the default constructor of the class it is extending, this also means that the subclass will have the parent's methods available to it.  
		studentNumber = 0;

	}
}

```

***

Lecture 5: 

* CONTINUING PPT 4 of Inheritance

* Sometimes it makes sense to have inheritance/hierarchy other times it's overkill(see hello world).

* The lower down on the subclass, the more specific it is, the higher up the superclass it is more generic

* Don't override/include methods/varialbes uneccessarilily because then you just override for no good reason

* You can however overLOAD a default constructor for instance:

```Java

public Student() {
	
	super();
	studentNumber = 0;	// This is overloading because person didn't/doesn't have a student number and compliments stuff
}

```

* Class hierarchy

* Every class is an extended/inherited class, wetehr or not it's declared to be

* Fields/methods in extended classes

* An object of an extended class contains two sets of variables/methods (fields/methods which are defined locally in the xtended class and fields/method which are inherited from the superclass)

* Constructors in extended classes

* A constructor of the extended class can invoke on of the superclass's constrocturs by using the super() method

* If no superclass constructor is invoked explicitly, then the superclass's no arg constructor super() is iinvoked automatically as the first statement of the extended class's constructor

* Constructors are NOT methods and NOT inherited

* Phases of Object construction

* When an object is created, memory is allocated for all of its fields which are set to default values which is then follwed by a three phase construction (Invokes a superclass's constructor, Intitalize the fields by using their intializers and intialization blocks, execute the body of the constructor).  

* Superclass's constructor is executed using the same 3 phase construcotr, this process is executed recursively until the Object class is reached

* Overlaoding and Overridng

* Overloading is good, overriding is something we want to use sparingly

* Overloading: providing more than one method with the same name, but a diff paramater list, this means you're adding a new method with the same name and a diff signature/paramater set/list

* Overriding: replacing the superclass's implementation of a method with your own deisgn, both the paramater lists and return types must be the same.  

* If an overriding method is invoked on an obj of the subclass then it's the subclass's version of the method that gets implemented, and overiding method can have a diff access specififer from the superclass's version, btu only wider accessibility is allowed (if it's private you can make it public, but not the other way around)

* A method can only be overridden if it's accessible in the subclass (e.g. i fth emethod is private in the superclass it can't be overridden, protected and public methods will/can be ovrridden though)

* Hiding fields

* Fields cannot be ovrrriden, they can only be hidden.  If a field is declared in the subclass and it has the same name as one in the superclass, then the field belongs to the superclass cannot be access directly by its name any more.  

* Polymorphism

* An object of a given class can have multiple forms, either as its declared class type, or any subclass of it.  

* An object of an extended class can be used wherever the original class is used

* When the class of the object decides the implementation to be used, that is polymorphism which is the same when you access the field

* The overridng methods throws clause can have fewer types listed than the method in the super class or more specific types


* Type Compatibility

* Java is a strongly typed language (which just means everything has a type, int, String, long, float, double, etc...)

* null object is compatible with all ref types

***

Lecture 6: More Abstract Methods and Interface Design


* Type conversions

* THere are 2 types widening (less specific AKA: Assigning a subtype to a supertype) and narrowing: converting a ref of a supertype into a ref of a subtype


 * Abstract classes and methods

 * Abstract methods are only declared but not concrete implementations are provided.  They need to be implemented by extending the class (they are implemented via subclasses) (Shape would be a good abstract class, we would put the basic concept of a thing in a shape, or the basic idea of a person in an abstract class)

* Each method which has no implementation in the abstract class must be declared as abstract and any class with abstract methods must be declared abstract

* When you extend an abstract class there are 2 situations, 1.  Leave some or all of the abstract methods still undefined, then the subclass must be declare abstract too. or 2: Define concrete implementation of all the inherited abstract methods, then the subclass is no longer abstract.  

* An object of an abstract class CANNOT be created

* Protected

* Allows subclass methdos to access a superclass field, making methods protected make more sense if the subclasses can be trusted to use the method correctly but other classes cannot.  

* A protected member is accessible within the class itself, within code in the same package, and it can also be accessed from a class through object refs that are of at least the same type as the class assuming refs of the class's type or one of its subtypes\

* Object: The ultimate superclass

* Utility methods of Object: Equlas(returns wether two obj refs have the same val), (hashcode, returns the hash code for the obj which is derived from the objs mem address), clone: returns a clone of the boj, getClass: return the expresson of the objs class which is a class obj, finalize: finalize the obj during garbage collection, toString: return a string representation of the obj

* Inheritance design hints

* Place common operations/fields in the superclass, try not to use protected fields, model IS-A relationships, don't use inheritance unless all inherited methods make sense, don't change expected behavior when overriding a method, Use polymorphism not type information

```Java

// The following is bad:

if (x is of type1) {
		action1(x);
} else if (x is of type2) {
		action2(x);
}

// If action1 and action2 are a common concept, make the concept a method of a common superclass/interface fo both types, and then call .action()

```

* INTERFACE DESIGN

* Concept 

* An interface, is a way to describe what classes should do without specifying how they should do it.  It's not a class, but a set of requirements for classes that want to conform to the interface

* An interface is a blueprint/template

```Java


/example

public interface Comparable {
	
	int compareTo(Object otherObject);
}

```

* Interface declaration

* Consists of interface keyword, its name, and the members 

* Similar to classes, interfaces can have 3 types of members: constants(fields), methods, nested classes/interfaces

* Interface member/constant fields 

* An itnerface can define named cosntatns which are public, static, and final automatically.  Interfaces never containt instance fields.  

* All the named constants MUST be initialized

```Java

Interface Verbose {
	
	int SILENT = 0;
	int TERSE = 1;
	int NORMAL = 2;
	int VERBOSE = 3;

	void setVerbosity (int level);
	int getVerbosity();
}

```

* Interface member methods are implicitly abstract.  So every method declaration consists of the method header and a semicolon.  

* Interface methods are implicitly public.  NO OTHER TYPES OF ACCESS MODIFIERS ARE ALLOWED (E.G. NOT FINAL OR STATIC)

* Implementing interfaces in a class

* Two steps to make a class implement an interface

1.  Declare that the class intentds to implement the given interface by using the implements keyword:

```
class Employee implements Comparable {
	
}

```

2.  Supply defs for all methods in the interface 

```
public int compareTo(Objec otherObject) {
	
	Employee other = (Employee) otherObject;
	if (salary < other.salary) return -1;
	if (salary > other.salary) return 1;
	return 0;
}


```


* Interfaces are generally used on HUGE projects, but for the most part we will use interfaces already defined by their classes


* If a class leaves any method of the interface undefined, the class becomes an abstract class and must be declared abstract

* A single class can implement multiple interfaces.  Just be sure to separate the interface names by a comma

```

class Employee implements Comparable, Cloneable {
	
	// Code here
}

```

* Instantiation properties of interfaces

* Interfaces are't classes, you can't use the new operator to instatiate an interface, you CAN declare interface variables though, BUT they must refer to an object of a class that implements the interface

```

class Employee implements Comparable {
	

}
x = new Employee();

```

* Interfaces support multiple inheratance and can extend more than one interface.  

* An extended interface inherits all the constants of its superintrfaces, so make sure when a subinterface inherits more than one constant with the same name, or when a sub and superinterface contain constants with the same name, to be sure to use sufficent information to refer to the target constant.  

* When an interface inherits two or more constatns with the same name be sure to use the superinterface name in the subinterface to refer to the constant of the superinterface


```

interface A {
	
	int val = 1;
}

interface B {
	
	int val = 2;
}

interface C extends A, B {
	
	System.out.println("A.val" = "+ A.val");
	System.out.println("B.val" = "+ B.val");
}

```

* IF a superinterface and a subinterface have two constants with the same name, then the one belonging to the superinterface is hidden.  You can access the subinterface version by using the name, and you can access the superinterface version by using the superinterface name followed by a dot, and then the constant name.  

* If a declared method in a subinterface has the same sig as an inherited method and the same return type, then the new declaration overrides the inherited method.  If the only difference is in the return type, then there will be a complie time error.  

* An interface can inherit more than one method with the same signature/return type.  A class can implement different interfaces containg methods with the same sig/return type.  

* Overriding in interfaces has no question of ambiguity.  The behavior is ultimatley decided by the implemntation in the class implementing them.  The real issue is wether a single implementation can honor all the contracts implied by that method in different interfaces

* Methods that have the same name but different paramater lists are overloaded.  

* An example of this would be an interface shape, with a class Point that implements shpae, and a sublcass of Point called Circle and another subclass called Cylinder

* Basically we use interfaces to provide multiple templates for the sam concept

* Tagging, cloning, and depp cloning, are a thing, but beyond the scope of the course.  



***

* LECTURE: !!!!!!!!!!!!


* Collections 

* Concept

* Collections/A collection is a data structure/object used to hold other objects and organize them in useful ways for efficent access

* The Java.util package provides a framework but programmers can also provide specific implementations like collections, map (dict, hash map, etc...)

* Methods available to collections

* size, isEmpty, contains, add, remove, equals, hashCode, iterator, toArray, etc...


* Iteration/Iterator

* Implementing the iterator method/interface access the elements of a collection without exposing its structure, but there no guarantees concerning the order in which elements are returned.

* The methods that iterator has available are hasNext(), next, and remove

* Iteration methods are already in the objects so you may as well use them

* ListIterator

* ListIterator extends the Iterator interface, by adding methods to manipulate an ordered list.  

* ListIterator has hasNext, hasPrevious, next, previous, nextIndex, previousIndex, remove, add, set available to it

* If the content of the collection is modified when the iterator is in use it can/will affect the values returned by the methods.

* If you need a snapshot of the collection, make a simple copy, java.util uses fail-fast iteratos which detect when a collection has been modified and throws an exception

* Assignment 3 ::: Create a stock object with different prices and put them in a stack and a queue

* List

* A list is an ordered collection which allows duplicats and goes from 0 to the list size - 1

* List is implemented by Arraylist and linked list which have different features and access times/tradeoffs

* Set and SortedSet

* The Set a collection that contains only UNIQUE elements. 

* SortedSet extends set to specify and will always return the elments in a specific order as determined by the Comparable order(Usually it's the natural order AKA: How they went in)

* The two implementations are Hashset(implemented using a hashatable) and Treeset(implemented using a balanced tree structure)

* Map/ Sortedmap

* Contains key value pairs, duplicate keys are not allowed and this is implmented by hashmap and treemap

* These are neccessary for associations

* If you iterate through key/value sets, they may return values in any order



* Synchronized Wrappers and the collections class

* Most of the collectiions impemented by java.util are unsynchronized, but you can use synchrnization wrappers for collections that might be access by multiple threads, which would prevent potential problems

* Implementations are by default unsynchronized, which can cause race condtions/starvation conditions(lack of access to resoruces because its taken by something else)

* Threads are running executions, and each object that is created runs its own separate thread.  Synchronize methods basically means 'play nice with others'.  Synchronizing adds overhead, but hopefully prevents errors

* Unmodifiable wrappers and the collections class

* Unmodifiable wrappers, basically makes a copy of the collection so that you can modify parts of it, but not update the original collection.  Think of it like a photocopy, you can modify the copy(writing on it etc...), but keep the origianl the same.  



```Java

private String suitsNames[] = {"Hearts", "Clubs", "Diamonds", "Spades"};

public final List suits = Collections.unmodifiableList(Arrays.asList(suit(s)Names))

```

* In the above, the original collection can still be used/changed, but the unmodifiable wrapper is still good


* Abstract implementations

* The collection f/w provides abstract implementations to design developer created implmentations of relevant collection interfaces to satisfy whatever may come up , this may be better for overwriting a whole thing.  It may be also better for something like a phone which has more limited resources, and only using a limited set of things means a smaller memory footprint

* Legacy collection types 


* Old -- comporable to


* Include enumerators -- iterator

* Vector -- Arraylist

* Stack -- subclass of Vector

* Dictoionary -- Map

* Hashtable -- Hashmap

* Properties -- subclass of Hashtable


***


* (Lecture 8A) (PPT 7: Exceptions/IO)

* Overivew of the hierarchy

* Exceptions extend Throwable, Throwable branches out into Error and Exception

* Error is an internal error/resoursce exhaustion inside Java.

* Exception splits into IO exception and Runtime exception

* Error checking is basicaly everything a user does, an Exception is everything a program does (for the most part)



* Exception focus

* Exceptions that drvie from runtimeException (bad cast, out of array access)

* The above happens because errors exsist in the program and are the programmers fault

* Exceptions not in the RuntimeExceptioin

* Issues such as a malformed URL, the program is fine, but other bad things happen, e.g. not your fault

* Checked vs. Unchecked exceptions

* Unchecked expcetions: (Exceptions derived from the Error class, or RuntimeException)

* Checked exceptions (All other exceptions that are not unchecked expcetions)  If these occur they must be dealt with in some way, and the compiler will check wether you provide exception handlers for checked exceptions that might occur.  

* Declaring to throw checked exceptions

* A java method or constructor should be declared to throw exceptions under two situations: A.  It calls another method that throws a checked exception or 2.  It throws a checked exception with the throw statement inside the body

* Declare a method/constructor th throw an exception(s) by using the throws clause in its header

```

public FileInputStream(String s) throws FileNotFoundException, IOException, EOFException

```

* You should not declare an unchecked exception after throws, they are either outside of your control or should be avoided completely by correcting your code.  

* Using throw to throw an exception

* Throw an exception ounder bad situations(E.g a file is too long/too short)

```

// Two ways to declare

throw(new EOFException());

EOFException e = new EOFException();
throw e;

```

* THe type of error thrown has to match that declared in the method header (either type or subtype)

* If you can find an appropriate exception class in the library you can use it, if not you can create your own exception type

* Creating new exception types

* Exceptions are objects.  New exception types hsould extend Exception or one of its subclasses

* We ceate new exception types because they can provide more detail and because they can provide information programmers on what actions to take/how to resolve the issue

* Catching exceptions

* Checked exceptions handingling is strictly enforced.  If you invoke a method that lists a checked exption in its throws clause there are 3 choices: A.  Catche and handle the excetpion.  B.  Declare the exception in the throws clause and let the exception pass through the method(where you might have a finally caluse to clean up things first).  C.  Catch the excetpion and map it into one of the excpetions by throwing an exception of  a type delcared in your own throws clause



* Try/Catch clause

```

try {
	
	// Statements
} catch (exceptionType1 identifier1) {
	
	// Handler for type1
} catch (exceptionType1 identifier 2) {
	
	//handler for type2
} ...

```

* If no exception occurs during the execution of the statments in the try clause, the above would finish sucesfully and the catch clauses are skipped.  

* If any of the code in the try block throws an exception either directly via a throw or indirectly by a method invoked in it: A.  The program skips the remaining code in the try block B.  The catch clauses are examined one by one to see if the type of thrown exception is compatabile with the type declared in the catc.  C.  If an appropriate catch is found, the code inside the body of that catch gets exectued and all the remaining catch clauses are skipped.  D.  If no acceptable catch is found the exception is thrown to an outer try that might have a catch clause to handle it.  

* A catch clause with a superclass ExcetpionType cannot preceede a catch clause with a subclass exceptionType


* Midterm is takehome, but answers should be straightforward (2-3 sentences)


***

### Lecture 9 (PPT 8): User interface components with Swing

* Swing Overview

* Classes from javax.swing defines Gui components including JLable, JTextField,JcheckBox,JComboBox,JList,Jpanel, etc...

* These components are written in Java so they have greater portability/flexibility than the original GUI package/components from Java.awt which is platform depenedent

* Keep in mind some swing components are platform depenedent such as JFrame.  

* Common superclasses are Object -> awt.Component - > awt.Container -> Javax.swing.Jcomponent

* Component class, the operations common to most GUI components are found in the Component class

* Two important methods originate in the Container class of Add (add components to a container), setLayou enables a program to specify the layout manager that helps a Container position/size its components

* Jlabel

* A Jlable object provides text instruction/information to a GUI and displays a linee of Read only text, an image or both text/image

* If you do not add a GUI component to a container, the GUI will not be displayed when the container appears on the screen.  

* To make an interactive GUI program

* There must be components (buttons, windows, menus, etc...), Events (Mouse click, window close, etc...), Event listeners (Interfaces), event handlers (methods etc...)/listeners

* Event handling model

* Some GUIs are event driven (e.g they generate events when the user interacts with the GUI mouse moving, clicking, typing, selecting an item etc...) Many of these events are defined in java.awt.event and javax.swing.event

* THree diff parts to the even handling mechanism: A. Source: The GUI component which the user inetracts.  B.  Event object: Encapsulated info about the occured event.  C.  Event listener: An object which is notified by the event source when an even occurs and provides responses to the event.  

* The programmer must perform 2 tasks to process a GUI event.  A.  Register an event listener which is an object of a class that implements one or more of the event listener interfaces from packages B.  Implement an event handling method

* Jtext field and JPasswordField are single line areas in which text can be intered by the user from the keyboard or text can be displayed

* When the user types data into them and presses enter an action even occurs.  If the program registers an event listener, the listener processes the event and can use the data in the text field at the time of the event in the program

* Buttons

* A button is a component the user clicks to trigger a specific action

* There are several types of buttons in Java which are all subclasses of AbstractButtion

* Command buttons generates actions, toggles have on/off values, check buttons generates ItemEvents, etc...

* Layout managment

* ALl components in a container are positionted by a layout manger.  BUttons are generally managed by the flow layout manger, which is the default layout manager for a panel

* THe default manager lines componets horizonatally unil there is no more room and then starts  new row of components, after resizing the container the layout manager reflows the components automatically.  The default is to center the components in each row.  You can choose alining to the left/right of the container

* Layout manger Using panel

* Potential problems include streched buttons for using broder layout, the solution is to use panels which acts as a container for interface elements and can be arranged inside a larger panel which uses flow layout

* To do this, create a panel, add components to the panel, and then add the panel to a larger container

```

JPanel p = new Jpanel();

p.add(button1);
p.add(button2);
p.add(button3);
frame.add(panel, BorderLayout.SOUTH);

```



***

### Lecture 10 video 

* Going over assignment 4: Create a text editor with a menu bar with File(Open, save As, exit) and Style 

* Everything with a J is Swing, everything that does not have J is AWT

* Garbage collection automatically looks at memory refs, sees what's not being used, and frees up the resource(s).  Garbage collection runs on an intermittent but regular basis, when it needs too.  


* All examples
    