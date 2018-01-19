# Derek Banas Java Video Tutorial Series

## 04/06/2017

### 1: Java Video Tutorial

```Java
// Java does not care about whitespace, it cares about the semicolon


public class Hello {
	
	// Class variable
	static String randomString = "String to print";

	// Constants are declared with final and by convention are all upper case
	static final double PINUM = 3.14529;

	public static void main(String[] args) {
		System.out.println("")


	/*
	* Primitive Data Types:
	*	byte
	*	short
	*	int
	*	long
	*	float
	*	double
	*	boolean(true or false)
	*	char(surrounded by '' if letter)(can also be \b, \t, \n etc... OR also 66(B), 65(A), etc...)
	*	Strings
	*/

	// Casting/Converting
	byte bigByte = 127;

	String byteString = Byte.toString(bigByte);
	String shortString = Byte.toString(bigByte);
	String intString = Integer.toString(bigByte);
	String longString = Long.toString(bigByte);
	String floatString = Float.toString(bigByte);
	String doubleString = Double.toString(bigByte);
	String booleanString = Boolean.toString(bigByte);

	double aDoubleVal = 3.142593;
	int - doubleToInt = (Int) aDoubleVal;	// 3, if the double is larger than the int, then the casting will hold as much as possible and possibly lose data




	}

}

```


```Java
// Derek Banas Java Video Tutorial 2

import java.util.*;

public class JavaLessonTwo {
	
	static Scanner userInput = new Scanner(System.in);
	
	public static void main(String[] args) {

		System.out.print("What is your favorite number? ");

		if (userInput.hasNextInt()) {
			// userInput in this case recieves the input the user typed and stores it in numEntered

			int numEntered = userInput.nextInt();

			System.out.println("You entered " + numEntered);
		}

	}

}


```