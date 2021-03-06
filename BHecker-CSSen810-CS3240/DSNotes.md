# Barbara Hecker - Data Structures/Algos Fall 2011

## https://www.youtube.com/watch?v=th00zpkPM9Q&index=1&list=PLC617CBC8385356FF

***

### Lecture 1

* ID aspects of software quality

* Introduce concept of data structs

* SW Dev

* SWE is the study of the techniquestheory that support the dev of HQ SW

* THe focus is on controlling the dev process to achieve consistent/good results

* Goals of SWE

* Solving the right problem, deliving a solution on time/under budget, deliver a HQ solution

* Physical example

* Consider the ### problem of storage containers being unloaded on a dock

* Containers could immediatley be loaded onto waiting trains/trucks, and is effiecnt for the workers etc...

* What do we know about the containters (ID, what they contain etc...)

* Containers could be offloaded and stored on the dock, which is efficnet for unloading but not efficnet for finding/loading storage containers onto trucks/trains, and requries a linear search of the entire storage area each time a container needs to be found

* What if we lay out a very large array so that each storage container is indexed by its ID? (ID is unique, but the array would be large and likely mostly empty and thus a significant waste of space)

* What if we use the array but allow the list to expand/contract to elim empty slots (array wld always be orderd by ID, finding a container would be easier, HOwever it would force containers to be used mitltiple times as containers are added/removed)

* If the ID gives us the dest of the container, what if we create an array of destinations where each cell in the array is an array of containers? (2x array/double array)

* The above would allow us to store the containers for each destinaton in a variety of ways (storing the order they are unlaoded with the first one unloaded being the first one shipped(queue), Shotre in the order they are unloaded with the last one unloaded being the first one shipped(Stack), Store by ID order within each destination(ordered list))

***


### Lecture 2: Analysis of Algos

* OBJs

* Discuss goals of SW dev w/ respect to efficency

* Itroduce concept of algo analysis

* Explore concept of asymptotic complexity

* Compare growth functions

* Analysis of Algos

* An aspect of SW quality is efficnet use of resources, and analysis algo is a core topic

* Algo analysis gives a basis to compare eficenc

* Growth functions

* Analysis is defined in geeral terms based on problem size, and the operation(search, sort, reverse, etc...)

* A growth function shows the relationship betweent eh size of a problem(n) and the time it takes to solve the problem

* It's not usually neccessary to know the exact growth function, but the main issue is the complexity, or how the use of resources grows as n increases

* The use of resources is determined by the dominant term in in the growth function(the factor)

* The order/Big O notation refers to the algorithmic complexity



```

Growth Function  |  Order  |  Label
----------------------------------------

t(n) = 17        | O(1)		| constant
----------------------------------------
t(n) = 3log(n)	| O(log n)	| logarithmic
----------------------------------------
t(n) = 20(n) - 4 | O(n)		| linear
----------------------------------------
t(n) = 12(n) log(n) + 100 (n) | n(log(n))
----------------------------------------
t(n) = 3^2 + 5(n) - 2 | O(n^2) | quadratic (A quadratic function is derived from the latin quadratus(square))
----------------------------------------- 
t(n) = 8(n^3) + 3(n^2) | O(n^3) | cubic
-----------------------------------------
t(n) = 2^n + 18(n^2) | O(2^n) | exponential 
-----------------------------------------


```

* The curve for growth functions regarding small values of N is constant/almost non-existant for n and log(n), but huge for 2^n and larges for n^3 (Input size N on the X, time on the Y).  In the middle (just above log(n)) is n (log(n)), then a huge distance away is (n^2) and then n^3 and then finally 2^n


* An example of complexity is a loop, if a loop executes X number of times, and then there is a loop nested under it the complexity of the outer loop INCLUDES the complexity of the inner loop


```Java

// Loop complexity = O(n), because the loop executes n times and the loop body is O(1)
for (int i = 0; i < n; i++) {
	
	x = x + 1;
}

// Loop complexity = O(n^2), because the loop execues n times and th body of the loop including a nested loop is O(n)
for (int i = 0; i < n; i++) {
	
	x = x + 1;

	for (int j = 0; j < n; j++) {

		y = y - 1;
	}
}

```


* Analyzing method calls

* To analyze method class, we replace the method call with the order of the body of the method(e.g. the following would be O(1)):

```Java

public void printsum(int count) {
	
	sum = count * (count + 1) / 2;
	System.out.println(sum);
}

```

* CHAPTER 3: Collections (Yay our first data structure!)

* Objs

* Define the concpet/terminoligy, explore basic struct of Java collections API, discuss the abstract design of collections, define a set collection, use a set collection to solve a prob, examine an array implementation of a set

* Collections

* A collection is an object that gathers and organizes other objects/elements

* Many fundamental collections exist, stats ques lists trees graphs, etc...(difference between a queue and a stack is the order)(Because with stacks you push and pop the last one on, with queues you push the last one and pop the first one)

* Collections can be broadly categorized as a linear(organizes the elements in a straight line) or nonlinear (think of a hierarchy tree)

* Collections are usually based on the order in which they were added to a collection or some other inherent relationship amon the elements(e.g. alphabetical order, first come first serve, etc...)

* Which type of collection you use depends on what you are trying to accomplish


* Abstraction

* Hides certain details at certain times(E.g. you don't have to know what's in a car engine to know what a car engine is)

* Provides a way to deal w/ system complexity

* A collection is an abstraction

* We want to separate the interface of the collection(how we interact with it) from the underlying details of how we choose to implement it

* Issues w/ Collections

* We need to consider how th collection operates conceptually, how do we design its interface, what kinds of problems does a collection help use solve, how might we implement the collection, what are the tradeoffs/costs/benefits of each implementation.  

* Terms

* Data type: A group of values and the operations defined on those types

* Abstract data type: A data type whose values/operations are not inherently defined in a programming language

* Data structure: The programming constructs used to implement a collection

* Java collections API

* The Java COllections API is a set of classes that represents some specific collection types, implemented in various ways and is part of a large Java class library

* Stack collection

* Keep in mind pretty much everything is a collection(Stacks, Queues, trees, etc.. are all collections)

* A stack arranges elements in a LIFO order (think of a stack of books, plates, etc..)

* You can only place new elements on the stack, and can only remove elements from the top of the stack

* Collection Ops

* Every collection has a set of operations that define how we interact w/ it

* For the user this usually menas how we add/remove elements and determine if the collection is empty, or determine the size of the collection

* Push(adds elements to the top of the stack), pop(removes an element from the top of the stack),peek(Examines the elements at the top of the stack),isEmpty(determines if the stack is empty).size(determines the number of elements of the stack)

* What do we store

* We could recreate our stack each time with a specific data type, but that would be inefficent

* Instad create the collection once and reuse it, but we must maintain type compatibiliity and checking

* Inheritance

* In general creating a new class via inheritance is faster, easier/cheaper

* Inheritance is at the  heart of software reuse

* Class comes from classifying groups of objects w/ similar charactersitics (Hey classes are another form of collection)

* We could define the mammal class that would describe state/behavior, and from that class we could define the hourse class that would inherit all the variables/methods of the mammal class while defining additional variables/methods of its own

* The above establishes an IS A relationship between the superclass and the subclass(A horse IS A mammal)

* Class hierarchies

* Multiple child classes can be defined from a parent/superclass which can lead to class hierarchies

* Inheritance(The Object class)

* In Java, all classes are dervied from the Object class

* The Object class provides a toString method that is usually overridden, and an equals method to test objects/aliases

* Polymorphism

* Having many forms

* A polymporphic refrence is a ref var that can ref to diff types of objects ad diff points in time

* The spec method invoked by a poly ref can change from one invoke to the next

* Polymorphism results in the need for dynamic inding, and is usually a bining of a call to the code which occurs at compile time.  

* Dynamic binding menas that the binding cannot occur until run time.  

```

Mammal pet;		// Key line here because although we declare pet as a mammal, it can also be assigned to/inherit information from the Horse we create
Horse secretariat = new Horse();
pet = secretariat;

```

* The above is polymorphic as a result of inheritance

* Using polymorphism via inheritance, a ref of type Object can ref to any object of any type

* Thus we could store Object refs in our stack allowing us to store objects of any type

```

Animal[] creatures = new Mammal[10];
creatures[1] = new Reptile();			// There should be issues here, but it does compile (because objects are all equivalent, we won't get a typecheck err)

```

* Using the object class does not provide a type safe solution for the collection because Java enables us to define a class based on a Generic object


* Generic Types

* If we assume that we need to define a class named Box that stores/manages other objects of type T

* We could create an instance of box to hold objects of the Widget class, but we could also create an instance of Box to hold objects of the Gadget class

* The type spplied at the time of instantiation rplaces the type T wherever it is used in th edeclaration of the class, a Generic type such as T cannot be instantiated.  

* Interfaces

* The programming construct in Java known as an interface is a convenienet way to define the operations on a collecion

* An interface lists the set of abstract methods that a class implements and provides a formal way to establish declarations that a class will respond to (method calls)


* Using stacks

* Stacks are helpful when solving certain problem types

* E.g. undo in most applications keeps track of the most recent changes/ops in a reverse order

* If we were to write something using postfix notation we would use a stack (e.g. what we want to do(the operation) would come after the things we want to do it to(the operands))

* E.g. Normally we would write things using infix notation such as (3 + 4) * 2.  But using postfix notation it would look like: 3 4 + 2 *.  

* In sentece for the above is: Take 3 and 4, and add them togheter, then take 2 and multiply it by 3 + 4

* To fully eval the postfix experssion we would scan from L to R, determining if the next toke is an operator or operand, if it is an operand we push it on the stack, if it is an operator we pop the stack twice to get teh two oeprands, perform the operation, and then push the rsult on the stack.  

* At the end of the stack there will boe only one value on the stack, which is the result

* Exceptions

* Collections must always manage problem situations carefully (such as isEmpty and attempting to remove something), can the structure be full(e.g. run out of resources/memory), this means that capacity setting/implementation is an issue

* Managing capacity

* An array has a specific capacity/number of cells when it is created(Most stacks in most languages are implemented as an array)

* The array's capacity is also the stack's capacity, but what do we do when the stack is full, but a new element is added(throw an exception, return a status indicator, automatically expand capacity?)

* The first 2 options requrie the user to pay attetnion, but the 3rd option is best especially in light of our desire to separate implementation from the interface.  

* Capacity is an implementation roblem and s/n be passed onto the user without good reason

* Exceptions

* Problems that arise in Java, and deines an unusual sitation

* A program can have 3 ways to handle exceptions(Not at all, where the issue occurs, deal with it later)

* If the issue is not handled the program will throw the exception and terminate

* If the program deals with it there, there will be a try/except block

* If the program deals with it later, it will usually return control to the method that called it

* Passing exceptions back is known as exception propogation, which continues until the exception is caught/handled or the program terminates


*** 

### Lecture 3: Collections(Continued)


* The ArrayStack Class

* Making the following decisions of maintaining an array of generic refs, the bootom of the stack i index 0, the elements of the stack are in order/contiguous, the integer var top stores the index of the next available slot in the array.  

* This approach allows the stack to grow and shrink at higher indicies

* An array queue implementation does not work as well as a stack

* Other ops that might matter include, size, isEmpty, and toString which prints out all the elements in a string format

* Analysis of ops

* Generally they are efficent, b/c push/pop is O(1), etc...

* Chapter 4: Linked Structures

* Obj

* Describe the use of refs to create linked structs

* Compare linked structs to array based structs

* Explore techniques for managing a linked list

* Discuss the need for sparate node to form linked structures


* Refs as Links

* There are many ways to implement a collection

* A linked structure uses object refs varaibles to link one object to another(as opposed to an index refrence)

* Recall that an object ref var stores the address of an object, which can be thought of/is a pointer to an object

* With a linked list there is no list, it's a collection/linking of objects

* Sef ref Objs

* A Person object for isntance could contain a ref variable to another Person object.  

* Linked Lists

* This type of ref can be used to form a linked list, in which one object refs to the next object, which refs to the next obj etc...

* Each obj in a list is often called a node

* A linked list is a dynamic data struct in that its size grows/shrinks as needed, unlike an array whose size is static

* Non linear structs

* A linked list is generally a linear structure, but it is flexible

* Obj refs also allow us to create non linear structs such as hierarchies and graphs

* Managing Linked lists

* The refs in a linked list must be managed to maintian integrity and ensure that the entry point into the list is properly maintained

* The order in which certain steps are taken is important

* Consider inserting/deleting nodes in various positions within the list

* Messing up things in a linked list can cost you branches, but losing things in an array can just cost you that one element.  

* Elements without Links

* THe problem w/ self ref objs is that they must know they are part of a list

* A better approach is to manage a separate list of nodes that also refs the objs stored in a list

* The list is still managed using the same techniques

* THe objs stored in the list need no special implementation to be part of the list

* A generic list collection can be used to store any kind of obj

* Sentinel nodes

* These are variations on the implentation of linked lists that have useful sitations, such as sentinel/dummy nodes on either end of the list, which eliminates the special cases of inserting/deleting the first/last node

* Doubly linked list

* In a doubly linked list each node has a ref to both the next and previous nodes in the list(as opposed to only a ref to the next obj in a single linked list), this makes traversing the list easier

* You can have quadruple, triple, etc... linked lists(these are largely trees)

* Implementing a stack with links

* We can use a linked list to implement our stack collection from CH3

* First though we need to create a LinearNode class to represent a node in the list (basically we only care about the beginning, because we push/pop from it)

* LinkedStack(Other operations)

* We could implement a search/peek function

* THe isEmpty operation returns true if the element count is 0, and false otherwise

* The size operation returns the count of elements in the stack

* The toString operation can be implemented by traversing the linked list

* Analysis of Stack Operation(s)

* Like ArrayStack ops, the LinkedStack ops work on one end of the collection and are gnerally efficent (e.g. push, pop, and other ops are O(1)) (Stacks are usually more efficent that queues)

* Classic use of a stack is to keep track of alternatives in maze traversal or other trial/error algorithims, using a stack in this way simulates recursion.  

* Run time enviros keep track of method calls by placing an activation rocord for each called method on the runtime stack, when a method complets its execuation, its popped from the stack and control returns to the method that called it.  This is how we can traverse a maze, by keeping track of the movements(this works for checkers, chess, etc...)

* The Java Collections f/w defines a Stack class w/ similar ops as derived from the Vector class and has some characteristics that are not quite a pure stack

* Java.util.stack has been around since the original Java release and has ben retrofitted to merge with the Collections f/w

* An interface gives functionality and psuedo-multi-line functionality/inheritance

* Assignment 1

```

CS 3240 Data Structures and Algorithms
Programming Assignment #1

Linked List


Write a program that can be used as a database of student’s information for a department. The program should be able to dynamically allocate or de-allocate storage for the student’s records using linked lists. You must use a linked list to keep the list of items for this program.

The database should have the following fields: the first and last names, a course code, and a grade for a student. You can use a struct, class or any data type of your choice to store the information.

The program should display the following menu:

Welcome to the database menu!

Press 1 to insert a new record
Press 2 to delete a record
Press 3 to search the database (by last name)
Press 4 to print a range in the database
Press 5 to find the class average for a course
Press 9 to quit

The insert function should work regardless of the position. Position 0 refers to the position before the first record. Any position greater than the length of the database should be put as the last position.

Similarly, the delete position should work for any position. Make sure that it works even when deleting the first, last or middle records.
The search function should be used to search by last name. If that student is found, all records associated with that student should be printed (on the screen).  The print function should work regardless of the range requested. If the start or end ranges are not defined, only the valid records should be printed. Hint: To compute the class average, first search the field with the course code. Only average those grades that match the proper course code.

Implement the above program in ANY programming language using any technique that you want to meet the requirements as described above.


```


### Lecture 4: Going through Java code for the assignment


``` Java

// Mystack

// This is an array implementation of a stack, keep in mind Arrays in Java are statically allocated

     
public class MyStack {
  private int maxSize;

  private long[] stackArray;

  private int top;

  public MyStack(int s) {
    maxSize = s;
    stackArray = new long[maxSize];
    top = -1;
  }

  public void push(long j) {
    stackArray[++top] = j;
  }

  public long pop() {
    return stackArray[top--];
  }

  public long peek() {
    return stackArray[top];
  }

  public boolean isEmpty() {
    return (top == -1);
  }

  public boolean isFull() {
    return (top == maxSize - 1);
  }

  public static void main(String[] args) {
    MyStack theStack = new MyStack(10); // make new stack
    theStack.push(20);
    theStack.push(40);
    theStack.push(60);
    theStack.push(80);

    while (!theStack.isEmpty()) {
      long value = theStack.pop();
      System.out.print(value);
      System.out.print(" ");
    }
    System.out.println("");
  }
}

```

```

Answering my own questions:

Wouldn't we always want to use an array, since arrays are usually First In Last Out? 
Sure, but that's still a stack implementation, and you could use a stack implementation for things like a maze/decision making etc...
Arrays are well and good, but understanding underlying data structures helps too

```


```Java

// ArrayList implementation


import java.util.ArrayList;

public class ArrayListEx {

    public static void main(String[] a) {

        //Creating a string array List
        ArrayList<String> arrayL = new ArrayList<String>();
        arrayL.add("Cat");
        arrayL.add("Car");
        arrayL.add("Brother");
        arrayL.add("Basket ball");

        System.out.println("\nThis is String ArrayList size of: "+arrayL.size()+"\n");

        for(int i=0;i<arrayL.size();i++){
            System.out.println(arrayL.get(i));   
        }

        System.out.println("\n=========================\n");

        //creating a Array list of students

        ArrayList<Student> studentList = new ArrayList<Student>();

        Student s1=new Student();
        s1.setName("John");
        s1.setAge(20);
        s1.setSchool("Harvard");
        s1.setMarks(88.9);

        Student s2=new Student();
        s2.setName("Bella");
        s2.setAge(22);
        s2.setSchool("Oxford");
        s2.setMarks(56.9);

        studentList.add(s1);
        studentList.add(s2);

        System.out.println("\nThis is Student ArrayList size of: "+studentList.size()+"\n");

         for(int i=0;i<studentList.size();i++){
            int temp=i+1;
            System.out.println("Details of Student "+temp);
            System.out.println("Name: "+studentList.get(i).getName());
            System.out.println("Age: "+studentList.get(i).getAge());
            System.out.println("School: "+studentList.get(i).getSchool());
            System.out.println("Marks: "+studentList.get(i).getMarks());
            System.out.println("---------------------------\n");
        }

    }
}

//Class of Student
class Student
{
    String name;
    int age;
    String school;
    double marks;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getSchool() {
        return school;
    }

    public void setSchool(String school) {
        this.school = school;
    }

    public double getMarks() {
        return marks;
    }

    public void setMarks(double marks) {
        this.marks = marks;
    }
}


```

* Why would we make the user create their own array?  We can use the ArrayList class in Java

* Array lists can hold any object you want if you don't explicitly typecast them:


```Java

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {


    ArrayList arrL = new ArrayList();
    
    arrL.add("Hello");
    arrL.add("#");
    arrL.add(1);
    arrL.add('a');
    arrL.add(12.2);
    
    for (int i = 0; i < arrL.size(); i++) {
      
      System.out.println(arrL.get(i));
    
    }
    

  }
}

```

* 