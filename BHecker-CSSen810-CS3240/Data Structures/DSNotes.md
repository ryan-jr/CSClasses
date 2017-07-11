# Barbara Hecker - Data Structures/Algos Fall 2011

## https://www.youtube.com/watch?v=th00zpkPM9Q&index=1&list=PLC617CBC8385356FF

***

### Lecture 1

* ID aspects of software quality

* Introduce concept of data structs

* SW Dev

* SWE is the study of the techniques/theory that support the dev of HQ SW

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

* OK so for the longest time I was confused as to what a list was.  A list is a sequenced order of distinct items (a repeated item is considered distinct).  Lists are esentially containers and are used for data structures such as queues, stacks, linked lists, etc...

* One of the most straightforward things you can do is create an arrayList of strings, loop through it and get strings out, but one of the more interesting implementations is creating a class of your own design (student in this case) with its own properties, fields, etc... and we can access each of them from within an array/array list

* Stack from util in Java uses pop and push rather than insert and delete, there is also a search in the stack

* Arrays are special in that they are not dynamic (AKA you have to declare the static size of an array when it is declared) whereas lists are generally dynamic in size.



***

### Chapter 5 Queues

* Objs: Examine queue proccessing, define a queue abstract data type, demonstrate how a queue can be used to solve problems, examine queue implementations and compare those implementations

* A queue is a collection whose elements are addded on one end and removed from the other, and queues are process in in a FIFO fashion, and elements are removed in the same order.  Basically any waiting line is a queue (checkout at a grocery store, cars at a stoplight, and assembly line)

* A queue is usually depicted horizontally, w/ one end of the queue is the rear where elemtns are added and the front end from which elemnts are remeoved (the front).  Stacks only operate at one end, queues operate at both ends of a line.

* Queue operations are enqueue/deque.  Enqueue is adding, dequeue is removing an element, pure queues d/n allow users to access elements in the middle, but toString is included in Java for convience.

* Typical operators include enqueue, dequeue, first, isEmpty, size, and toString

* A queue can be used to help us encode/decode messages (e.g. Ceaser's Cipher).

* A repeating key is a series of ints that determins how much each char is shifted (e.g. the repeating key 3 1 7 4 2 5) would mean the first char is shifted 3, next 1, then 7, etc... and when the key is exhausted we start over at the beginning of the key.  (This could also be done w/ an array

* We could use the queue to store the key values, and dequeue a value as needed, and after using a key value we just enqueue it back onto the end of the queue so that way it will represent a constant key cycle.

* We could use a queue to simulate waiting in line and trying to figure out an algo to keep wait times below 7 minutes assuming customers arrive every 15 seconds, and that proccessing a customer takes 2 mins per cashier

* The linked queu class is similar to a stack in that a queue can be implemented using an underlying array or linked list.  The linked version of a queue can use the LinearNode class again.  In this implementation we keep a ref to the beginning of the list and will keep a second ref to the end, along with an integer ctr to keep track of the number of eements in the queue

* Other operations of a linked queue include first(returns a ref to the element at the front of the queue), isEmpty, size, and toString

* Queues can be implemented with an array to fix oen end of the queue at position 0 like we did with ArrayStack.  Since queues operate on both ends, it would force the shifting of elmeents either on enqueue or deque which means a better approach would be to use a 'circular' array and not fix either end of the queue

* If we d/n fix one end of the queue at index 0 we w/n have to shift the elements.  This is essentially a circular queue which is an implementation of a queue using an array that conceptually loops around on itself (the last index precedes index 0).  We keep track of integers that indicate where the front/rear of the queue are at any given time.

* Note that we can do a circular queue, but not a circular stack because we always know the last item of a stack (LIFO).

* When an element is enqueued in a circular queue the value of the rear must be incremented, AND it must take inot account the need to loop back to 0 (rear = (rear + 1} % queue.length;).  NOTE: The array implementation may reach capacity and need embigenning.

* Enquue is O(1) for both implementations, and deque is O(1) for linked and circular arrays but O(n) for the noncircular array version due to the need to shift elements.


***


### Lecture 6: Lists

* Lists are linear collections like stacks/quues but are more flexible.  Adding/removing elements in lists a/n restricted by the collection structure (e.g. you d/n have to operate at one end or the other). 3 specific types of lists (ordered, unordered, indexed)

* Ordered lists are orderd by some inherent charactersitic of the elements (alphabetic order, sequential order, etc...).  E.g. the elements themselvs determine where they are stored in the list.  

* Unorder lists the order is not based on element characteristics, the user determines the order, and a new element can be added to the front, rear or inserted anywhere in the list.  

* Indexed lists(Array lists), in an indexed lists elments are refed by their numeric position in the list, it's like an unordered list, but there is no inherent relationship among the elements and the user can determine the order AND every time the list changes the indexes are updated.  
 
 * List ops include removing, checking status, first, last, contains, isEmpty, size.  Stacks/queues are predetermined, lists generally care about order/implementaiton.  
 
 * Add is particular to an ordered list, add to front, add to rear and addafter are particular to an unordered list.  
 
 * List operations, have java interfaces to define collection ops.  Recall that interfaces can be defined via inheritance, and we define common list ops in one interface and then derive 3 others from it that define the interfaces of the list types.  
 
 * We could use lists to create a round robin tournament (best team against worst team, second best,against second worst, etc...), keep track of teams/individual team members, etc...
 
 * Josephus problem: set of elements are in a circle, starting w/ a particular elemnt every ith element is removed, proccessing continues until only one element left.  Given the starting point and the remove count(i), which element is left?
 
 * An array implementation of a list could follow similar strats to those used for a queue by fixing one end of the list index at 0 and shift it as needed when an element is added/removed, or a circular array could be used to avoid the shift at one end (However, there is no avoiding the shift if an element is added/removed in the middle)
 
 * As with a stack anc queue we can implement a list collection w/ an underlying linked list
 
 * Doubly linked lists has 2 refs in each node, one to the next element in th elist and one to the previous element which makes moving back/forth in a list easier and eliminates the need for a previous refrence in certain algos, but there is more overhead in managing such a list.  
 
 * The remove method for the doubly linked list is more elegant than the singly linked list, but such elegance comes at the overhead cost with storing/managing additional links.  Singly is more explicit.
   
  * In both array and linked implementations most operations are simiar efficency (O(1)).  This is true EXCEPT when shifting or searching happens in whcih case they are O(n).  Depending on the situation the frequencey of need for particular ops may guide the use of one approach over another.  (Add/remove stuff on a regular basis = ArrayList, adding stuff constantly = linked list)
  
  * Java lists include the List interface, Vectors, ArrayList, and LinkedList.  
  
  ***

  ### Chapter/Lecture 7: Recursion


  * Explain recursion concepts, examine recursive methods/steps, define inf recursion/how to avoid it, explain when recursion should/should not b used, demonstrate using recursion to solve problems.  

  * Recursion is a technique in which a method can call itself to solve a problem.  For example a recursive defition is one which uses the word/concept being defined to define itslef.  In some situations a recursive def can be an appropriate way to express a concpet.  

  * All recrusive defs must have a non recursive part/base case otherwise it results in an infinite loop/recursion.  

  * Mathematical functions can be defined recursively (think factorials), which are things like 1! = 1, or N! = N * (N - 1)!.  A factorial is defined in terms of another factorial until the base case is reached.  

  * A method in Java can invoke itself and setup a recursive method.  The code of a recursive method must be structure to handle the recursive and base case.  Each call sets up a new execution enviro w/ new paramaters/local vars.  When the method complets control returns to the method that invoked it (usually another instance of itself). 

 ```Java

public int sum (int sum) {
	
	int result;
	if (num == 1) {

		result = 1;
	} else {

		result = num + sum(num - 1);
	}
	return result;
}

 ```

* In terms of recrusion v iteration, we don't always have to use recursion.  E.g. normally we would not use recursion to figure out the sum of a factorial because the iterative solution is easier to understand.  EVERY recursive solution has a corresponding iterative solution.  RECURSION has the drawback of overhead of multiple method calls/invocations, BUT sometimes recursion solutions are more simple/elegan than iterative solutions

* A method invoking itself is considered to be direct recursion, but a method could invoke another method, which invokes another, etc... until the original is invoked again(m1 calls m2, which calls m3, which calls m1 again) which is known as indirect recursion (this is often harder to debug/trace)

* Recursion can be used for maze traversial by marking each location encoutered as 'visited' and attempt to find a pthat from the 'visited' location's unvisted neighbors.  Recursion would be used to keep track of the path(s) through the maze using a runtime stack with the base cases being a blocked move, or arrival at the end.  

* The towers of Hanoi is a classic recursion problem as a puzzle made up of 3 vertical pegs and several disks that slide onto the pegs.  The disks are different sizes and placed on one peg w/ the largest disk on the bottom and increasingly smaller disks up to the top.  The goal is to move all of the disks from one peg to another following the rules: Only one disk can be moved at a time, a disk cannot be placed onto a smaller disk, and all disks must be on some peg.  

* (Cont), the towers of Hanoi recursion would look like: To move a stack o N disks from the original peg to the destination peg: Move the topmost N-1 disks from the original peg to the extra peg, move the largest disk from the original peg to the destination peg, move the N-1 disks from the extra peg to the destination peg.  The base case occurs when a 'stack' contains one disk.  

* (Cont), Note that the number of moves increases exponentially as the number of disks increase, the recurisve solution is straightforward/elegant to program with the iterative solution being more complex.  

* When analyzing a loop, we determine the order of the loop body and multiply it by the number of times the loop is executed.  This is similar to recursive analysis, we determine the order of the method body and multiply it by the order of recurstion (order of recrusion is the number of times the recursive definition is followed).  For the Tower of Hanoi the size of the problem is the number of disks and the operation of interst is moving one disk, which means that except for the base case each recursive call result sin calling itself twice more (to solve a problem of N disks we make 2^n - 1 moves).  This means that the algo is O(2^n) (exponential complexity)


***

### Lecture/Chapter 8: Searching and Sorting

* Searching is the process fo finding a target element among a group of items, or determining if it is not there.  This requires repeatedly comparing the target agains tthe cnadidates in the elements you're searching (the search pool).  An efficent sort performs no more comparisons than needed.  

* For the comparable interface we want to define the algos such that they can search any set of objects which contains compareTo, which is designed to return an integer that specifies the relationship between two objects (obj1.compareTo(obj2)).  This call returns a number less than, equal to, or greather than 0 if obj1 is less than, equal to, or greater than obj1 respectively.  

* To use the comparable interface objects must be comparable to each other, meaning they must be of the same class or descendants of the same ancestor.

* Linear search examines each item in the search pool, one at a time, until either the target is found or nothing is left.  Linear search does not assume the items in the search pool are in any particular order, we just need to be able to examine each item in turn.  Straightforward, but inefficent.

* If the search pool is sorted, then we can be more efficent than a lienar search.  A binary search eliminates large parts of the search pool w/ each comparison.  Instead of starting in the middle we start in the middle.  If the target i/n found we know that if it is in the pool at all, it is in one half or the other, we can then jump to the middle of that half and continue similarly.  

*  Binary searches are often implemented recursively w/ each recursive call searching a smaller portion of th epool.  The base case is running out of viable candidates to search which means the target is not in the pool.  At any point there may be 2 middle values, in which case either could be used.  

* In comparing search algos a linear search, on average, would examine n/2 elements before finding the target, and therefore a linear search is O(n).  The worst case for binary search is (log(2)n) comparisions.  Binary search is lograthmic with a time complexity of O(log(sub 2)n), however, the search pool must be sorted, and for arbitrarily large n's a binary search is must faster.  

* Sorting is the process of arranging a group of items into adfined order based on particular criteria, Sequential sorts require about n^2 comparisiions to sort n elements, whereas logarithmic sorts typically require n(log(sub 2)n) comparisons.

* Selection sort orders a list of values by repetively putting a particular value into its final position.  Selection sort, finds the smallest value in the list, switches it with the value in the 0th position, find the next smallest value in the list, switch it with the 1st position, repeat until all values are in their proper places.  

* Insertion sort orders a list of values by repetitively insertign a particular value into a sorted subset of the list.  If a sorted sublist was of length one, we would insert the second item into the sorted sublist, shifting hte first item as needed, and repeat the previous steps neccessary for each subsequent element we want to insert.  Because of shifting this can cause more 'movement' (aka processing)

* Bubble sort, orders a list by comparing neighboring elements and swapping positions as needed.  Bubble sort scans the list, exchanging adjacent elements if they are not in relative order, which bubbles the highest value to the top.  This repeats for the second highest value, until all elements have been placed in proper order.  

* Insertion, slection, and bubble sort all use nested lopps and perform n^2(roughly) and are relativley inefficnet.  

* Quick sort orders a list of valus by partitioning the lsit around one element, then sorting each partition.  Choose one element in the list to be a partition element, organize the elements so that all elements less than the partition are to the left, and all greater are to the right, and apply the quick sort algo to each half of the partition.  The choice of the partition element is arbitrary, for efficency it would be nice if the partition element divided the list roughly in half, the algo will work in any case however.  The work can best be thought of as 2 methods, quicksort which does the recursive algo and find Partition, which rearranges the elemnts into 2 partitions.  

* Merge sort order a list of vals by recurisvely divindg the list in half until each sublist has one element, and then recombining things.  Merge sort divides the list into 2 roughly equal parts, recurisvely divides each part in half until a part contains only one element, merge the two parts into one sorted list, and contineu to merge parts as the recursion unfolds.  

* Both quickSort and mergeSOrt use a recursive structure that takes log(sub2(n)) steps to decompose the original lists into lists of lenght one, at each step, both algos either compare or merge all elements, therefore both algos are O(n(log(n))).  

* Radi sort uses queus to order a set of values.  A queue is create for each possible value of a postion/digit in the sort key.  E.g. if the sort key is a lowecase alphabetic string, there would be 26 queues, or if there was a decimal integer, there would be 10 queus corresponding to the digits 0 - 9.  Each pass throught he sort examines a particular position in the sort value, the elemnet is put on the que corresponding to that positions value, proccessing starts w/ the least signification portion (e.g. 1's or A's) to the most significant position.  This algo is easy to get wrong, but can be more efficent in some cases

***

### Lecture/Chapter 9: Trees

* A tree is a non-linear structure defined by the concept that each node in the tree, other than the first/root node, has exactly one parent.  for trees, operations are dependent on the type of tree and its use.  Efficency is measured by how quickly it takes to find something, trees are another type of collection that is represented differently.  (e.g. simiarl to liked lists via nodes, but represnted differently/non-linear)

* Common vocab: A node refres to a location in the tree where an element is stored, and a root: which refers to the node at the base of the tree or the one node in the tree that d/n have a parent.  

* Each node of the tree points to the nodes that are directly beneath it in the tree (refered to as children).  A child of a child is a grandchild, and a child of a grandchild is called a great-grandchild.  A node that does not have at least one child is a leaf, and a node that is not the root and has at least one child is an internal node.  

* Any node below another node and on a path from that node is a descendant of that node, any node above another node on a connecting path from the root to that node is an ancestor, all children of the same node ar siblings, a tree that limits each node to no more than n childeren is an n-ary tree.  The n-ary tree is usually done to limit search space and potentially create a balanced tree, where each node has the same number of children

* Each node of the tree is at a specific level/depth within the tree, the level of a ndoe is the length of the path from the root to the node.  The path length is determined by counting the number of links that must be followed to get from the root to the node.  The root is considered as level 0, children level 1, grandchildren level 2, and so on.  

* The height/order of a tree is the length of the longest path from the root to a leaf, thus the order of the tree from root A to leaf F is 3(b/c C is its own separate leaf), the path from root A to leaf C is 1

* A tree is 'balanced' if all the leaves of the tree are roughly at the same depth.  

* The concept of a complete tree is related to teh balance of a tree, and a tree is considered complete if it is ablanced and all the leaves at level H are on the left side of the tree.  While this is a seemingly arbitrary concept, there are implications for how the tree is stored in certain implementations.  

* There are general startegies for implementing trees, with the most straighforward being a linked structure with each node being part of the TreeNode class(e.g. much like with LinearNode class for linked lists).  Each node would contain a pointer to the element to be stored in that node as well as pointer for each of the possible children of the node, and depending on the implementation it may also be useful to store a poitner in each node to its parent.  

* For certain types of trees (specifically binary trees) a computational strategy can be used for string a tree using an array.  For any element stored in position n of the array, that element's left child would be stored in position ((2 * n) + 1) and the elements right child would be stored in position (2 * (n + 1 ))  

* For trees implemented via arrays, this strategy can be managed in terms of capacity in much the same way that we did for other array-based collections, but there are some drawbacks, e.g. if the tree that we are storing is not relatively complete we may be wasting large amounts of memory allocated to the array for portions of the tree that do not contain data.  

* [This](http://imgur.com/BFYKb2o) is an array strategy for implementing trees.  Note how the root(element A, position 0 in the array) is 0, and then we move from left to right in the tree implementation, and how there is wasted space for positions 5 and 6.  Note how the tree is/can be represented/searched in a linear fashion, but how storing the tree in an array structure limits the data that can be held.  

* A second possible array implementation of a ree is modeled after the way OS's manage memory.  Instead of assigning elements of the tree to array position by location in the tree, array postions are allocated contiguously on a first come, first serve basis.  Each eelemtn of the array will be a node class similar to the TreeNode class from earlier, but instead of storing obect ref vars as pointer to its children(and possibly parent), each node would store the array index of each child(and possibly its parent).  Such an approach allows elements to be stored contigusously so as to not waste space, but increases overhead(b/c if elements are deleted the remaining elements would have to be shifted for continuity)

* [This](http://imgur.com/a/YlwNj) is a linked strategy for an array implementation of trees, notice how A connects to 2 and 1(it's children), and C has nothing(no children)

* Trees are a useful/efficent way to implement other collections.  For instance with lists the general case for find operations is O(n), but if we implemented an ordered list using a balance binary search tree, a binary tree w/ the added proerty that the left child is always less than the parent which is always less thatn/equal to the right child, then we could improve the efficency of the find op to O(log(n)).  

* (CONT) the height/order of a tree's search space will always be log(sub2(n)), where n is the number of elements in the tree, for any n-ary tree w/ n elements the tree's height will be log(sub(n)(N)).  Wit the added ordering property of a binary search tree, you are guaranteed to at worst search one path from the root to a leaf.   

* Four basic algos for traversing a tree (preorder(preset), inorder, postorder, and levelorder(traversal))

* Preorder traversal is accomplished by visiting each node, and its children starting w/ the root.  (Psuedocode): Visit node, traverse(left child), traverse (right child).  

* Inorder traversal is accomplisehd by visiting the left child of the node, then the node, then any remaining child nodes starting w/ the root.  (Psuedocode): Traverse(left child), visit node, traverse(right child).  

* (Basically bottom up) Postorder traversal is visiting the children, then the node starting w/ the root.  (Psuedo code) Traverse left child, traverse right child, visit node

* Levelorder traversal(think of visiting a row in a database), is visiting all the nodes at each leve, one level at a time, starting with the root.  

* Binary trees usually have a set of common operations, but in order to have an add operation we need to know how the tree will be used.  

* Binary trees can be implemented with links, which is similar to linked lists which has links to all of the children. 

* THe find method in a binary tree is a good example of recursion, which works well because the tree is a 'controlled' environment (e.g. you know the depth)

* Binary tress can also be implemented via arrays 


* Compilers actually take expressions and turn them into a tree and traverses it and puts it into an Abstract Syntax Tree, via parsing it and puting into tokens/lexameans and evaluates things via a prefix/postfix methodology.  

****

Lecture 10: Binary Search Trees

* Binary search trees are binary trees w/ the added property that for each node, the left child is less than the parent and less than or equal to the right child, this allows us to do more operations on the tree such as Add since we know where in the tree an element would go.  

* Removing an element in a binary search tree requires finding the element to be removed, if the element is not a leaf, replace it with its inorder successor, return the element removed.  

* There are 3 cases for the location of the minimum element in a binary search tree (and removing it).  1.  If the root has no left child then the root is the minimum element and the right child of the root becomes the new root.  2.  If the leftmost node of the tree si a leaf, then we se its parents left child refrence to null.  3.  If the leftmost node of the tree is an internal node, then we se its parents left child refrence to point to teh right child of the node to be removed. 

* The assumption of balanced binary search trees is important it gives us the structure of the tree, and being unablanced would affect the order of the tree.  A BST that would be unbalanced is a degenerate binary tree, and would be far less efficent than a balanced tree (O(n) vs O(log(n))).  

* There are multiple approaches to balancing such a tree  including brute force (inorder traversal of a fil and then using recursion to go back trhough the file/tree).  

* A better solution would be using algos such as red black/AVL trees that maintain a persistant balance of the tree and use rotations to maintain that balance.  

* A tree rotation is an operation on a binary tree that changes the structure WITHOUT interfering with the order of the elements

* Remeber balance is when all the leaf nodes are at the same level.  Right rotation (24:30), left rotation (26:30).  RightLeft rotation(28:00), LeftRight(30:00)

* AVL trees keep track of the difference in height between the right and left subtress for each node.  The difference in height is called the balance factor.  If the balance factor of any node is less than -1 or greater than 1, then the subtree needs to be rebalanced.  The balance factor of any node can only be changed through either insertion or deltion of nodes in the tree.  

* If for instance the balance factor of a node is +2 it means the right subtree has a path that is too long, and if the balance factor of the right child is +1 then it means the long path is the right sub-tree of the right child and a left rotation of the right child around the original node will solve the imbalnce

* Red/Black trees provide another alternative implementation of balanced binary search trees.  RBL trees are a balance BST where each node stores a color(usually stored as a boolean) with the following rules: THe root is black, all children of a red node are black, every path from the root to a leaf contains the same number of black nodes.  

* Insertion into RBLTrees(39:00)

* The concept is using colors to balance the trees (kind of like on/off bits) and if the colors are off then we rotate the tree.  

*  A set is a grouping of data, but a map is a key/value pair of data

***

### Lecture 11: Graphs and Trees

* A graph is a finite set of nodes(verticies) with edges between nodes.  A verticie would be each node, and an edge would be the lines between each node.  When x,y is an edge we say x is adjacent to y

* Nodes represent entities (people, places, things, etc...), edges represent relationships between x and y( x is bigger than y, x is faster than y)

* If directions of the edges matter than we show the edge directions and it is a directed graph.  If relationships by the edges are edges if x is a sibling of y, then its an undirected graph

* A path is a sequence of nodes such that there is an ege from each node to the next one in the sequence.

* A cycle in a graph is a path where the last node is the same as the first node

* An undirected graph is connected when there is a path between every pair of nodes, otherwise it is disconnected. 

* A rooted tree is a tree where one of the nodes is designated as the root node (only one root in a tree).  A rooted tree has a top down structre w/ the root on top, followed by nodes, adjacent to it right below, followed by nodes adjacent to those and so on.

* Nodes that are adjacent to and below x are considered children(with x being  the parent).  A node w/ no children is a leaf.  THe descendents of a node are itself, its children, their children etc..The ancestors of a node are: itself, its parent, its grandparent all the way up to the root

* THe depth of a node is the number of edges from the root to that node.  The depth/height fo a rooted tree is the depth of the lowest leaf

* A tree is a binary tree if every node has at most two children.  (0, 1, or 2 are all valid, 3 or more makes it NOT a binary tree).  We generally add left to right.  

* A binary tree has 3 parts, data, pointer to left child, pointer to right child (basically think of a doubly linked list)

* A binary search tree is a binary tree where every node holds a data value (a key).  For any node x all keys in the left subtree of x are less than/equal to x, for any node x all the keys in the right subtree of x are greater than the x key

* Insertion into a BST is searching a BST, the position is to the L/R of child of some node x.  Create a new node and create the appropriate pointer field.  

* Deletion from a BST is searching for b in tree T.  call X, the first node found to contain b.  If x is a leaf, remove x and set the appropriate pointer in the parent of x to null.  If X has only one child, y, remove x, and the parent of x becomes a direct parent of y.  If x has 2 children, go to the left subtree and find the largest node there, call it y, the node y can be found by tracing the rightmost path until the end (Note that y is either a leaf or has no right child).  Copy the data field of y onto the data field of x, and delete node y.  

* One tree traversal technique is a heap 

* Traversal is visiting every node at least once, and entails doing some processing of that node.  

* 3 recursive techniques fro binary tree traversal, and in each of them the left subtree is traveled recursively, the right subtree is traveled recursively, and the root is visited.  What makes each of these different is the order of recursion/traversal.  

* In preorder, the root is visitied before the subtree traversals (1.  Visit the root, traverse left subtree, traverse right subtree).  In inorder traversal, the root is visitied in-between left and right subtree traversal (1.  Traverse left subtree, visit the root, traverse right subtree).  In preorder traversal, the root is visited after the subtree traversals(1.  Visit the left subtree, 2.  Visit the right subtree 3.  Visit the root).  


* 30:31


